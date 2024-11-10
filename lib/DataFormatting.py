"""
    資料格式化
    將csv檔案彙整成要寫入資料庫的格式
    
    資料放置位置 ../opendata/
        裡面有資料夾 data0 ~ data41
        每個資料夾裡面有許多csv檔案
"""
"""
### 資料表與結構
| csv檔案中的欄位名稱 | 資料庫欄位名稱 | 資料型別 | 預設值 | 備註                                |
|------------------|--------------|---------|-------|------------------------------------|
|                  | city_code    | string  |       | 縣市代號 （參照params.py的city字典Key）|
|                  | city_name    | string  |       | 縣市名稱 （參照params.py的city字典Key）|
|                  | town_code    | string  |       | 鄉鎮市區參照params.py的town字典key）   |
| 鄉鎮市區          | town_name    | string   |       | 鄉鎮市區參照params.py的town字典value   |
| 交易標地          |trade_sign    | int      |       |（房地 => 1 建物 => 2 土地=> 3 車位=>4, 房地+車位 => 5）|
| 土地位置建物門牌    |address        |strnig    |      |                                     |
| 交易年月日          | trade_date   | int      |       |                                    |
| 成交總價(元)        |price_total   | int      |      |                                     |
| 單價元平方公尺       | price_nuit   | int      |     |                                      |
| 建物移轉總面積平方公尺 | total_area   | float     |     |                                     |
| 編號                  | code         | string    |     |                                     |
| 屋齡                  | age          | int       |  0  | 此處比較特特別，假測現在開啟的檔案是a_lvr_land_a.csv要取這份檔案中的「編號」欄位的值，然後到a_lvr_land_a_build.csv這份檔案對應的「編號」取得屋齡，如果是土地就沒有屋齡問題預設值為0|
"""

import csv
import os
import sys
import traceback
import re 
from typing import Dict, List
import json  # 加入 json 模組

# 添加父目錄到系統路徑，以便導入 params.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import params

class DataFormatter:
    def __init__(self):
        # 交易標的對應
        self.trade_type = {
            'land': 3,   # 土地
            'build': 2,  # 建物
            'park': 4,   # 車位
            'all': 1,    # 房地
            'all_park': 5,  # 房地+車位
            'rental': 6   # 租賃
        }
        
        # 直接使用 params.py 的對照表
        self.city_dict = params.city
        self.town_dict = params.town
        
        # 新增：記錄建物屋齡對照表
        self.building_ages = {}
        
        
        # 新增：儲存所有處理後的資料
        self.all_data = []

        self.town_codes = params.town  # 從 params.py 取得鄉鎮市區代碼對照表

    def _update_town_codes(self, data: List[Dict]) -> List[Dict]:
        """更新所有資料的鄉鎮市區代碼"""
        try:
            for item in data:
                if not item['town_code'] and item['town_name']:  # 如果 town_code 為空但有 town_name
                    city_code = item['city_code']
                    town_name = item['town_name']
                    
                    # 在 params.town 中查找對應的代碼
                    if city_code in self.town_dict:
                        for town in self.town_dict[city_code]:
                            if town['title'] == town_name:
                                item['town_code'] = town['code']
                                break
            
            return data
            
        except Exception as e:
            print(f"更新鄉鎮市區代碼時發生錯誤: {str(e)}")
            traceback.print_exc()
            return data

    def _convert_price(self, price_str: str) -> int:
        """將價格字串轉換為整數"""
        try:
            if not price_str or price_str.isspace():
                return 0
            # 移除逗號和空白，轉換為整數
            return int(price_str.replace(',', '').strip())
        except (ValueError, AttributeError):
            return 0
        
    def get_file_info(self, file_name: str) -> Dict:
        """從檔案名稱獲取檔案資訊
        
        Args:
            file_name: 檔案名稱 (例如: a_lvr_land_a)
            
        Returns:
            Dict: 包含城市代碼、名稱和交易類型的字典
        """
        try:
            # 解析檔案名稱第一個字母作為城市代碼
            city_code = file_name[0].upper()
            
            # 從 params.py 獲取城市名稱
            city_name = self.city_dict.get(city_code, '')
            
            # 根據檔案類型決定交易類型
            if file_name.endswith('_c'):
                trade_type = self.trade_type['rental']  # 租賃
            elif file_name.endswith('_b'):
                trade_type = self.trade_type['all']  # 預售屋通常是房地交易
            else:
                trade_type = self.trade_type['all']  # 一般房地交易
                
            return {
                'city_code': city_code,
                'city_name': city_name,
                'trade_type': trade_type
            }
            
        except Exception as e:
            print(f"獲取檔案資訊時發生錯誤: {str(e)}")
            return {
                'city_code': '',
                'city_name': '',
                'trade_type': 0
            }

    def get_trade_type(self, trade_type_str: str) -> int:
        """根據交易標的字串判斷交易類型
        
        Args:
            trade_type_str: 交易標的字串
            
        Returns:
            int: 交易類型代碼
                1: 房地
                2: 建物
                3: 土地
                4: 車位
                5: 房地+車位
                6: 租賃
        """
        try:
            if '土地' in trade_type_str and '建物' not in trade_type_str:
                return 3  # 純土地
            elif '建物' in trade_type_str and '土地' not in trade_type_str:
                return 2  # 純建物
            elif '車位' in trade_type_str and '房地' not in trade_type_str:
                return 4  # 純車位
            elif '房地' in trade_type_str and '車位' in trade_type_str:
                return 5  # 房地+車位
            elif '房地' in trade_type_str or ('土地' in trade_type_str and '建物' in trade_type_str):
                return 1  # 房地
            else:
                print(f"警告: 無法識別的交易標的類型 '{trade_type_str}'，使用預設值 1")
                return 1  # 預設為房地
                
        except Exception as e:
            print(f"判斷交易類型時發生錯誤: {str(e)}")
            print(f"交易標的字串: {trade_type_str}")
            return 1  # 發生錯誤時返回預設值

    def get_town_info(self, city_code: str, address: str) -> Dict:
        """從地址取得行政區資訊
        
        Args:
            city_code: 城市代碼
            address: 完整地址
            
        Returns:
            Dict: 包含行政區代碼和名稱的字典
        """
        # 取得該城市的行政區對照表
        town_dict = dict(self.town_dict.get(city_code, {}))
        
        # 尋找地址中符合的行政區名稱
        for code, name in town_dict.items():
            if name in address:
                return {'code': code, 'title': name}
        
        # 找不到則回傳空值
        return {'code': '', 'title': ''}
        
    def process_directory(self, directory_path: str) -> List[Dict]:
        """處理目錄中的所有檔案"""
        try:
            all_data = []
            build_files = []
            main_files = []
            
            # 第一步：分類檔案
            for filename in os.listdir(directory_path):
                if not filename.endswith('.csv'):
                    continue
                    
                file_path = os.path.join(directory_path, filename)
                
                # 將檔案分類
                if '_build.csv' in filename:
                    build_files.append((filename, file_path))
                else:
                    main_files.append((filename, file_path))
            
            # 第二步：處理所有建物檔案，建立屋齡對照表
            for build_filename, build_file_path in build_files:
                main_filename = build_filename.replace('_build.csv', '.csv')
                self.load_building_ages(build_file_path, main_filename)
            
            # 第三步：處理主要檔案
            for filename, file_path in main_files:
                file_info = self.parse_filename(filename)
                if file_info:
                    data = self.process_file(file_path, file_info)
                    all_data.extend(data)
            
            # 第四步：更新 town_code
            all_data = self._update_town_codes(all_data)
            
            return all_data
            
        except Exception as e:
            print(f"處理目錄時發生錯誤: {str(e)}")
            traceback.print_exc()
            return []

    def process_file(self, file_path: str, file_info: Dict) -> List[Dict]:
        """處理單個檔案"""
        try:
            results = []
            
            with open(file_path, 'r', encoding='utf-8') as f:
                # 讀取中文欄位名稱作為 fieldnames，並移除 BOM 標記
                fieldnames = next(f).strip().split(',')
                fieldnames[0] = fieldnames[0].replace('\ufeff', '')  # 移除 BOM
                
                # 跳過英文欄位名稱
                next(f)
                
                # 使用中文欄位名稱建立 DictReader
                reader = csv.DictReader(f, fieldnames=fieldnames)
                
                print(f"\n使用的欄位名稱: {fieldnames}")  # 印出欄位名稱以供確認
                
                for row in reader:
                    # 根據檔案類型選擇對應的處理方法
                    if '_a.csv' in file_path:
                        result = self._process_a_file_row(row, file_info)
                    elif '_b.csv' in file_path:
                        result = self._process_b_file_row(row, file_info)
                    elif '_c.csv' in file_path:
                        result = self._process_c_file_row(row, file_info)
                    else:
                        continue
                        
                    if result:
                        results.append(result)
                        
            return results
            
        except Exception as e:
            print(f"處理檔案時發生錯誤: {str(e)}")
            print("檔案路徑:", file_path)
            traceback.print_exc()
            return []
    
    def load_building_ages(self, build_file: str, main_file: str):
        """讀取建物檔案並建立屋齡對照表"""
        try:
            print(f"\n開始讀取建物檔案屋齡資訊...")
            print(f"建物檔案: {build_file}")
            
            with open(build_file, 'r', encoding='utf-8') as f:
                # 讀取中文欄位名稱作為 fieldnames
                fieldnames = next(f).strip().split(',')
                fieldnames[0] = fieldnames[0].replace('\ufeff', '')  # 移除 BOM
                print(f"建物檔案欄位名稱: {fieldnames}")  # 印出欄位名稱以供確認
                
                # 找出編號和屋齡的欄位索引
                code_field = None
                age_field = None
                for field in fieldnames:
                    if '編號' in field:
                        code_field = field
                    elif '屋齡' in field:
                        age_field = field
                        
                if not code_field or not age_field:
                    print(f"警告：找不到必要的欄位")
                    print(f"編號欄位: {code_field}")
                    print(f"屋齡欄位: {age_field}")
                    return
                    
                print(f"使用的欄位名稱 - 編號: {code_field}, 屋齡: {age_field}")
                
                # 跳過英文欄位名稱
                next(f)
                
                # 使用中文欄位名稱建立 DictReader
                reader = csv.DictReader(f, fieldnames=fieldnames)
                
                # 清空之前的屋齡對照表
                self.building_ages = {}
                
                for row in reader:
                    if not row:  # 跳過空行
                        continue
                        
                    # 取得編號和屋齡
                    code = row.get(code_field, '').strip()
                    age_str = row.get(age_field, '').strip()
                    
                    if code and age_str:
                        try:
                            age = int(age_str)
                            if age >= 0:
                                # 將編號中的區域代碼統一轉換為 FAI
                                code = re.sub(r'F[A-Z]B', 'FAI', code)
                                self.building_ages[code] = age
                                print(f"新增屋齡對照: 原始編號={row.get(code_field, '')}, 轉換後編號={code}, 屋齡={age}")
                            else:
                                print(f"警告: 無效的屋齡值 {age} (編號={code})")
                        except ValueError:
                            print(f"警告: 無效的屋齡格式 '{age_str}' (編號={code})")
                
            print(f"\n建物屋齡對照表建立完成，共 {len(self.building_ages)} 筆")
            if self.building_ages:
                print("建物屋齡對照表中的前5筆資料:", list(self.building_ages.items())[:5])
            else:
                print("警告：建物屋齡對照表是空的！")
                
        except Exception as e:
            print(f"讀取建物檔案時發生錯誤: {str(e)}")
            traceback.print_exc()
            
    def _process_building_row(self, row: Dict):
        """處理建物檔案的單筆資料
        
        Args:
            row: CSV 檔案的一列資料
        """
        try:
            # 取得編號
            code = row.get('編號', '')
            
            # 取得建築完成年月
            construction_date = row.get('建築完成年月', '')
            
            if code and construction_date and construction_date.strip():
                try:
                    # 假設建築完成年月格式為 YYYMMDD（民國年）
                    year = int(construction_date[:3])  # 取得民國年
                    current_year = 113  # 當前民國年（可以根據需要調整）
                    age = current_year - year
                    
                    if age >= 0:
                        self.building_ages[code] = age
                        print(f"新增屋齡對照: 編號={code}, 屋齡={age}")
                    else:
                        print(f"警告: 計算出負數屋齡 {age} (編號={code})")
                except ValueError:
                    print(f"警告: 無效的建築完成年月 '{construction_date}' (編號={code})")
            else:
                if not code:
                    print("警告: 找不到編號")
                if not construction_date:
                    print("警告: 找不到建築完成年月")
                    
        except Exception as e:
            print(f"處理建物資料列時發生錯誤: {str(e)}")
            print("原始資料:", row)

    def read_csv(self, file_path: str) -> List[Dict]:
        """讀取CSV檔案並轉換格式"""
        data = []
        try:
            filename = os.path.basename(file_path)
            file_info = self.parse_filename(filename)
            
            if not file_info:
                return data
            
            # 根據檔案類型選擇處理方法
            if '_build.csv' in filename:
                process_row = self._process_build_file_row
            elif '_land.csv' in filename:
                process_row = self._process_land_file_row
            elif '_park.csv' in filename:
                process_row = self._process_park_file_row
            else:
                # 分開處理 _a, _b, _c 結尾的檔案
                if filename.endswith('_a.csv'):
                    process_row = self._process_a_file_row
                elif filename.endswith('_b.csv'):
                    process_row = self._process_b_file_row
                elif filename.endswith('_c.csv'):
                    process_row = self._process_c_file_row
                else:
                    process_row = self._process_main_file_row
                    
            # 讀取並處理CSV檔案
            with open(file_path, 'r', encoding='utf-8') as file:
                # 跳過前兩行（標題行）
                next(file)
                next(file)
                reader = csv.DictReader(file)
                
                # 打印每一行資料以確認其內容
                for row in reader:
                    # print("原始資料行:", row)
                    processed_row = process_row(row, file_info)
                    if processed_row:
                        data.append(processed_row)
                        
        except Exception as e:
            print(f"讀取檔案 {file_path} 時發生錯誤: {str(e)}")
            
        return data

    def parse_filename(self, filename: str) -> Dict:
        """解析檔名取得城市代碼和交易類型
        
        Args:
            filename: 檔案名稱 (例如: a_lvr_land_a.csv, b_lvr_land_c.csv)
                
        Returns:
            Dict: 包含城市代碼和交易類型的字典
        """
        try:
            # 分割檔名 'a_lvr_land_a.csv' -> ['a', 'lvr', 'land', 'a', 'csv']
            parts = filename.split('_')
            
            # 取得城市代碼 (第一個字母)
            city_code = parts[0].upper()
            
            # 取得交易類型
            if '_build' in filename:
                trade_type = self.trade_type['build']
            elif '_land' in filename and len(parts) > 4:  # a_lvr_land_a_land.csv
                trade_type = self.trade_type['land']
            elif '_park' in filename:
                trade_type = self.trade_type['park']
            else:  # 主要檔案 (a_lvr_land_a.csv, b_lvr_land_c.csv 等)
                trade_type = self.trade_type['all']
                    
            return {
                'city_code': city_code,
                'city_name': self.city_dict.get(city_code, ''),
                'trade_type': trade_type
            }
        except Exception as e:
            print(f"解析檔名出錯: {filename}, 錯誤: {str(e)}")
            return None

    def _get_file_pattern(self, main_file_name: str) -> str:
        """根據主檔案名稱取得對應的檔案模式
        例如: 'd_lvr_land_a.csv' -> 'd_lvr_land_a_{type}.csv'
        """
        if not main_file_name.endswith('.csv'):
            return ''
        
        base_name = main_file_name[:-4]  # 移除 '.csv'
        if not base_name.count('_') >= 3:  # 確保檔案名稱格式正確
            return ''
        
        return f"{base_name}_{{}}.csv"  # 回傳可以填入類型的模式


    # def _process_main_file_row(self, row: Dict, file_info: Dict) -> Dict:
    #     """處理主要檔案的資料列"""
    #     try:
    #         print("\n處理資料列:")
    #         print("原始資料:", row)
            
    #         # 將 row.values() 轉換為列表以便索引
    #         values = list(row.values())
            
    #         # 取得各欄位值（使用索引位置）
    #         town_name = values[0]  # 鄉鎮市區
    #         trade_type_str = values[1]  # 交易標的
    #         address = values[2]  # 土地位置建物門牌
    #         trade_date = values[7]  # 交易年月日
    #         total_area = values[14]  # 建物移轉總面積平方公尺
    #         price_total = values[20]  # 總價元
    #         price_unit = values[21]  # 單價元平方公尺
    #         code = values[26]  # 編號 (serial number)
            
    #         print(f"取得編號: {code}")  # 除錯訊息
            
    #         # 從建物屋齡對照表查詢屋齡
    #         age = self.building_ages.get(code, 0)
    #         print(f"查詢屋齡: 編號={code}, 屋齡={age}")
            
    #         # 處理價格資訊（確保數值正確）
    #         try:
    #             price_total = int(price_total.replace(',', ''))
    #             price_unit = int(price_unit.replace(',', ''))
    #             total_area = float(total_area.replace(',', ''))
    #         except (ValueError, AttributeError):
    #             price_total = 0
    #             price_unit = 0
    #             total_area = 0.0
            
    #         # 判斷交易類型
    #         trade_type = self.trade_type['all']
    #         if '土地' in trade_type_str:
    #             trade_type = self.trade_type['land']
    #         elif '車位' in trade_type_str:
    #             trade_type = self.trade_type['all_park']
            
    #         # 使用地址取得行政區資訊
    #         town_info = self.get_town_info(file_info['city_code'], address)
            
    #         result = {
    #             'city_code': file_info['city_code'],
    #             'city_name': file_info['city_name'],
    #             'town_code': town_info.get('code', ''),
    #             'town_name': town_name,
    #             'trade_sign': trade_type,
    #             'address': address,
    #             'trade_date': trade_date,
    #             'price_total': price_total,
    #             'price_unit': price_unit,
    #             'total_area': total_area,
    #             'code': code,
    #             'age': age
    #         }
            
    #         print("處理結果:", result)
    #         return result
            
    #     except Exception as e:
    #         print(f"處理資料列時發生錯誤: {str(e)}")
    #         print("原始資料:", row)
    #         import traceback
    #         traceback.print_exc()
    #         return None

    def _process_a_file_row(self, row: Dict, file_info: Dict) -> Dict:
        """處理 a_lvr_land_a.csv 檔案的資料列"""
        try:
            # print("\n處理 a 檔案資料列:")
            # print("原始資料:", row)
            
            # 檢查是否已經是處理過的資料
            if 'city_code' in row:
                return row
                
            # 取得各欄位值
            town_name = row['鄉鎮市區']  # 第1欄
            trade_type_str = row['交易標的']  # 第2欄
            address = row['土地位置建物門牌']  # 第3欄
            trade_date = row['交易年月日']  # 第7欄
            total_area = row['建物移轉總面積平方公尺']  # 第15欄
            price_total = row['總價元']  # 第18欄
            price_unit = row['單價元平方公尺']  # 第19欄
            code = row['編號'].strip()  # 倒數第3欄
            
            # print(f"\n取得的欄位值:")
            # print(f"鄉鎮市區: {town_name}")
            # print(f"交易標的: {trade_type_str}")
            # print(f"地址: {address}")
            # print(f"交易年月日: {trade_date}")
            # print(f"建物移轉總面積: {total_area}")
            # print(f"總價元: {price_total}")
            # print(f"單價元/平方公尺: {price_unit}")
            # print(f"編號: {code}")
            
            # 從建物屋齡對照表查詢屋齡
            age = self.building_ages.get(code, 0)
            # 印出編號跟屋齡
            print(f"編號: {code}, 屋齡: {age}")
            
            # 處理價格資訊
            try:
                price_total = int(price_total.replace(',', ''))
                price_unit = int(price_unit.replace(',', ''))
                total_area = float(total_area.replace(',', ''))
            except (ValueError, AttributeError):
                price_total = 0
                price_unit = 0
                total_area = 0.0
                
            # print(f"\n處理後的價格資訊:")
            # print(f"總價元: {price_total}")
            # print(f"單價元/平方公尺: {price_unit}")
            # print(f"總面積: {total_area}")
                
            # 處理交易標的類型
            trade_type = self.get_trade_type(trade_type_str)
            # print(f"交易標的類型: {trade_type}")
            
            # 取得行政區資訊
            town_info = self.get_town_info(file_info['city_code'], address)
            # print(f"行政區資訊: {town_info}")
            
            result = {
                'city_code': file_info['city_code'],
                'city_name': file_info['city_name'],
                'town_code': town_info.get('code', ''),
                'town_name': town_name,
                'trade_sign': trade_type,
                'address': address,
                'trade_date': trade_date,
                'price_total': price_total,
                'price_unit': price_unit,
                'total_area': total_area,
                'code': code,
                'age': age
            }
            
            # print("\n最終處理結果:", result)
            return result
            
        except Exception as e:
            print(f"處理 a 檔案資料列時發生錯誤: {str(e)}")
            print("原始資料:", row)
            traceback.print_exc()
            return None

    def _process_b_file_row(self, row: Dict, file_info: Dict) -> Dict:
        """處理 b 檔案的資料列"""
        try:
            # 檢查是否已經是處理過的資料
            if 'city_code' in row:
                return row
                
            # 取得各欄位值
            town_name = row['鄉鎮市區']
            trade_type_str = row['交易標的']
            address = row['土地位置建物門牌']
            trade_date = row['交易年月日']
            total_area = row['建物移轉總面積平方公尺']
            price_total = row['總價元']
            price_unit = row['單價元平方公尺']
            code = row['編號']
            
            # 從建物屋齡對照表查詢屋齡
            age = self.building_ages.get(code, 0)
            print(f"建物屋齡: {age}")
            
            # 處理價格資訊
            try:
                price_total = int(price_total.replace(',', ''))
                price_unit = int(price_unit.replace(',', ''))
                total_area = float(total_area.replace(',', ''))
            except (ValueError, AttributeError):
                price_total = 0
                price_unit = 0
                total_area = 0.0
                
            # 處理交易標的類型
            trade_type = self.get_trade_type(trade_type_str)
            
            # 取得行政區資訊
            town_info = self.get_town_info(file_info['city_code'], address)
            
            result = {
                'city_code': file_info['city_code'],
                'city_name': file_info['city_name'],
                'town_code': town_info.get('code', ''),
                'town_name': town_name,
                'trade_sign': trade_type,
                'address': address,
                'trade_date': trade_date,
                'price_total': price_total,
                'price_unit': price_unit,
                'total_area': total_area,
                'code': code,
                'age': age
            }
            
            # print(f"最終處理結果: {result}")
            return result
            
        except Exception as e:
            print("處理 b 檔案資料列時發生錯誤:", str(e))
            print("原始資料:", row)
            return None

    def _process_c_file_row(self, row: Dict, file_info: Dict) -> Dict:
        """處理 a_lvr_land_c.csv 檔案的資料列 (租賃)"""
        try:
            # 檢查是否已經是處理過的資料
            if 'city_code' in row:
                return row
                
            # 取得各欄位值
            town_name = row['鄉鎮市區']
            trade_type_str = row['交易標的']
            address = row['土地位置建物門牌']
            trade_date = row['租賃年月日']
            total_area = row['建物總面積平方公尺']
            price_total = row['總額元']
            price_unit = row['單價元平方公尺']
            code = row['編號']
            # rental_type = row['出租型態']
            
            # 處理價格資訊
            try:
                price_total = int(price_total.replace(',', ''))
                price_unit = int(price_unit.replace(',', ''))
                total_area = float(total_area.replace(',', ''))
            except (ValueError, AttributeError):
                price_total = 0
                price_unit = 0
                total_area = 0.0
                
            # 取得行政區資訊
            town_info = self.get_town_info(file_info['city_code'], address)
            
            result = {
                'city_code': file_info['city_code'],
                'city_name': file_info['city_name'],
                'town_code': town_info.get('code', ''),
                'town_name': town_name,
                'trade_sign': 6,  # 租賃固定使用 6
                'address': address,
                'trade_date': trade_date,
                'price_total': price_total,
                'price_unit': price_unit,
                'total_area': total_area,
                'code': code,
                'age': 0,  # 租賃資料沒有屋齡
                # 'rental_type': rental_type  # 額外加入出租型態
            }
            
            return result
            
        except Exception as e:
            print(f"處理 c 檔案資料列時發生錯誤: {str(e)}")
            print("原始資料:", row)
            traceback.print_exc()
            return None
    
    def _process_land_file_row(self, row: Dict, file_info: Dict) -> Dict:
        """處理土地檔案(a_lvr_land_a_land.csv)的資料列"""
        try:
            # 取得編號 (第一個值)
            code = list(row.values())[0]
            
            # 取得土地位置 (第二個值)
            address = list(row.values())[1]
            
            # 取得土地移轉面積 (第三個值)
            try:
                total_area = float(list(row.values())[2].replace(',', ''))
            except (ValueError, AttributeError):
                total_area = 0.0
            
            # 使用地址取得行政區資訊
            town_info = self.get_town_info(file_info['city_code'], address)
            
            result = {
                'city_code': file_info['city_code'],
                'city_name': file_info['city_name'],
                'town_code': town_info.get('code', ''),
                'town_name': town_info.get('title', ''),
                'trade_sign': self.trade_type['land'],
                'address': address,
                'trade_date': '',  # 土地檔案沒有交易日期
                'price_total': '',  # 土地檔案沒有價格資訊
                'price_unit': '',
                'total_area': total_area,
                'code': code,
                'age': '0'  # 土地沒有屋齡
            }
            
            print("土地檔案處理結果:", result)
            return result
            
        except Exception as e:
            print(f"處理土地資料時發生錯誤: {str(e)}")
            print("原始資料:", row)
            return None

    def _process_park_file_row(self, row: Dict, file_info: Dict) -> Dict:
        """處理車位檔案(a_lvr_land_a_park.csv)的資料列"""
        try:
            # 取得編號 (第一個值)
            code = list(row.values())[0]
            
            # 取得車位類別 (第二個值)
            park_type = list(row.values())[1]
            
            # 取得車位價格 (第三個值)
            try:
                price_total = int(list(row.values())[2].replace(',', ''))
            except (ValueError, AttributeError):
                price_total = 0
            
            # 取得車位面積 (第四個值)
            try:
                total_area = float(list(row.values())[3].replace(',', ''))
            except (ValueError, AttributeError):
                total_area = 0.0
            
            result = {
                'city_code': file_info['city_code'],
                'city_name': file_info['city_name'],
                'town_code': '',  # 車位檔案沒有地址資訊
                'town_name': '',
                'trade_sign': self.trade_type['park'],
                'address': '',
                'trade_date': '',  # 車位檔案沒有交易日期
                'price_total': price_total,
                'price_unit': '',
                'total_area': total_area,
                'code': code,
                'age': '0'  # 車位沒有屋齡
            }
            
            print("車位檔案處理結果:", result)
            return result
            
        except Exception as e:
            print(f"處理車位資料時發生錯誤: {str(e)}")
            print("原始資料:", row)
            return None

    def _process_build_file_row(self, row: Dict, file_info: Dict) -> Dict:
        """處理建物檔案(a_lvr_land_a_build.csv)的資料列"""
        try:
            # 取得編號 (第一個值)
            code = list(row.values())[0]
            
            # 取得屋齡 (第二個值)
            age = list(row.values())[1]
            
            # 取得建物移轉面積 (第三個值)
            try:
                total_area = float(list(row.values())[2].replace(',', ''))
            except (ValueError, AttributeError):
                total_area = 0.0
            
            result = {
                'city_code': file_info['city_code'],
                'city_name': file_info['city_name'],
                'town_code': '',  # 建物檔案沒有地址資訊
                'town_name': '',
                'trade_sign': self.trade_type['build'],
                'address': '',
                'trade_date': '',  # 建物檔案沒有交易日期
                'price_total': '',  # 建物檔案沒有價格資訊
                'price_unit': '',
                'total_area': total_area,
                'code': code,
                'age': age
            }
            
            print("建物檔案處理結果:", result)
            return result
            
        except Exception as e:
            print(f"處理建物資料時發生錯誤: {str(e)}")
            print("原始資料:", row)
            return None
    


if __name__ == '__main__':
    formatter = DataFormatter()
    
    # 取得目前檔案的絕對路徑
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 構建資料目錄的絕對路徑
    directory_path = os.path.join(os.path.dirname(current_dir), 'opendata', 'datatest')
    
    # 確認目錄是否存在
    if not os.path.exists(directory_path):
        print(f"目錄不存在: {directory_path}")
        print("請確認以下事項：")
        print("1. opendata 資料夾是否在正確位置")
        print("2. datatest 資料夾是否存在")
        print("3. 目前的工作目錄:", os.getcwd())
        sys.exit(1)
    
    all_data = formatter.process_directory(directory_path)
    
    # 將資料儲存為 JSON 檔案
    output_path = os.path.join(os.path.dirname(current_dir), 'output')
    # 確保輸出目錄存在
    os.makedirs(output_path, exist_ok=True)
    
    # 儲存完整資料
    json_file = os.path.join(output_path, 'all_data.json')
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n處理完成，共有 {len(all_data)} 筆資料")
    print(f"完整資料已儲存至: {json_file}")
    
    if len(all_data) > 0:
        # 儲存範例資料（前10筆）
        sample_file = os.path.join(output_path, 'sample_data.json')
        with open(sample_file, 'w', encoding='utf-8') as f:
            json.dump(all_data[:10], f, ensure_ascii=False, indent=2)
        
        print(f"範例資料（前10筆）已儲存至: {sample_file}")
        
        print("\n前三筆資料範例:")
        for i, data in enumerate(all_data[:3]):
            print(f"\n資料 {i+1}:")
            for key, value in data.items():
                print(f"{key}: {value}")