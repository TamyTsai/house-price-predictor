from collections import defaultdict
from datetime import date

class Tools:
    '''
    工具類別，提供一些工具函數
    '''

    def changeToSelectDict(self, data):
        '''
        將GUI的輸入內容轉換成Select.createQuery方法可用的字典
        '''
        ageMap = {
            None: None,
            1: [0, 5],
            2: [5, 10],
            3: [10, 20],
            4: [20, 30],
            5: [30, 40],
            6: [40, 9999999],
        }
        #換算金額單位
        priceUnit = 10000 if data['pmoney_unit'] == 1 else 1
        minPrice = data['minp'] * priceUnit if data['minp'] != None else ""
        maxPrice = data['maxp'] * priceUnit if data['maxp'] != None else ""
        #換算台蘋或平方公尺
        areaUnit = 3.305785 if data['unit'] == 2 else 1
        minArea = data['mins'] * areaUnit if data['mins'] != None else ""
        maxArea = data['maxs'] * areaUnit if data['maxs'] != None else ""
        
        # 日期格式化
        begin = f"{data['p_startY']}{data['p_startM']}"
        end = f"{data['p_endY']}{data['p_endM']}"
        
        return {
            "city_code": data['city'],
            "town_code": data['town'],
            "trade_sign": data['ptype'],
            "address": data['p_build'],
            "trade_date": [begin, end],
            "price_nuit": [minPrice, maxPrice],
            "total_area": [minArea, maxArea],
            "age": ageMap[data['avg_var']]
        }
    
    def getKeyByDict(self, data):
        '''
        將資料中的交易日期，取年月，並將坪單價加總後再取平均值
        '''
        groupData = defaultdict(lambda: [0, 0])
        
        for item in data:
            key = str(item["trade_date"])[:5]
            key = int(key)
            groupData[key][0] += item['price_nuit']
            groupData[key][1] += 1
        
        averaged_data = {
            key: groupData[key][0] / groupData[key][1]  # 平均值 = 總價格 / 次數
            for key in groupData
        }

        sorted_data = dict(sorted(averaged_data.items()))

        return sorted_data
        