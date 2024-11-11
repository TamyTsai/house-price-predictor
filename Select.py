import mysql.connector
from mysql.connector import Error
import json
import calendar

class MySQL:
    '''
    提供MySQL的封裝類別
    在初始化時自動連接、並在結束時自動釋放連線
    提供select與delete與insert封裝方法，確保預防資料庫注入攻擊
    '''
    host = "162.241.253.231"
    user = "omeiliau_nou"
    password = "Nou@8089"
    database = "omeiliau_nou"

    def __init__(self):
        """在初始化時連接資料庫"""
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("成功連接到資料庫")
        except Error as e:
            print(f"連接資料庫失敗: {e}")
            self.connection = None

    def query(self, sql, params=None):
        """
        執行查詢並返回結果
        with MySQL() as db:
            result = db.query("SELECT * FROM lvr_lnd WHERE column = %s", (value,))
        """
        results = []
        if self.connection:
            try:
                cursor = self.connection.cursor(dictionary=True)
                cursor.execute(sql, params)
                results = cursor.fetchall()
            except Error as e:
                print(f"查詢失敗: {e}")
            finally:
                cursor.close()
        return results

    def __enter__(self):
        """允許 with 語句使用此類別"""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """結束時自動關閉連線"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("資料庫連線已關閉")

def adjust_trade_date(trade_date):
    """
    根據提供的 trade_date （如 '10901' 或 '11310'）來調整為完整的日期格式：
    起始日期後加上 '01'（即設置為該月的第一天）。
    結束日期加上 '31' 或 '30'，取決於該月的天數。
    """
    # 將日期字符串拆分為年份和月份
    year = str(trade_date)[:3]  # 年份前三位
    month = str(trade_date)[3:5]  # 月份後兩位

    # 構建起始日期：以該月的01號作為起始
    start_date = f"{year}0{month}01"

    # 根據年份和月份來確定該月的最後一天
    # calendar.monthrange 返回該月的天數
    _, last_day = calendar.monthrange(int(year) + 1911, int(month))  # 月份是從 1 開始
    end_date = f"{year}0{month}{last_day}"

def save_to_json(data, filename="query_result.json"):
    """
    將查詢結果保存為 JSON 檔案
    :param data: 查詢結果
    :param filename: 要儲存的檔案名稱，預設為 query_result.json
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"資料已成功保存為 {filename}")
    except Exception as e:
        print(f"保存檔案時出錯: {e}")

conditions = {
    "city_code": "A",
    "town_code": "A02",
    "trade_sign": ["1", "4"],
    "address": "大安路",                # 非必填
    "trade_date": ["10901", "11310"],  # 起始與結束日期
    "price_nuit": ["", ""],            # 非必填
    "total_area": [20, 40],            # 非必填，範圍條件
    "age": [5,10]
}

# 動態 SQL 查詢語句
query = "SELECT * FROM lvr_lnd WHERE "
query_conditions = []
params = []

# 處理條件
for column, value in conditions.items():
    # 跳過空值和 None
    if value is None or value == "":
        continue

    if isinstance(value, list):  # 如果條件是列表，處理範圍或 IN 查詢
        if column == "trade_date" and len(value) == 2:  # 處理日期範圍
            start_date, end_date = adjust_trade_date(value[0]), adjust_trade_date(value[1])
            query_conditions.append(f"{column} BETWEEN %s AND %s")
            params.append(start_date)  # 起始日期
            params.append(end_date)  # 結束日期
        elif column == "total_area" and len(value) == 2 and value[0] != "" and value[1] != "":  # 處理 total_area 範圍
            query_conditions.append(f"{column} BETWEEN %s AND %s")
            params.append(value[0])  # 起始值
            params.append(value[1])  # 結束值
        elif column == "price_nuit" and value != ["", ""]:  # 處理 price_nuit 範圍
            start_price, end_price = int(value[0]), int(value[1])
            query_conditions.append(f"{column} BETWEEN %s AND %s")
            params.append(start_price)  # 起始值
            params.append(end_price)  # 結束值
        else:
            # 處理其他列表條件，使用 IN 子句
            placeholders = ', '.join(['%s'] * len(value))  # 生成與列表長度匹配的佔位符
            query_conditions.append(f"{column} IN ({placeholders})")
            params.extend(value)  # 將列表中的每個值加入到 params
    elif column == "address" and value:  # 處理 address 欄位且非空
        query_conditions.append(f"{column} LIKE %s")
        params.append(f"%{value}%")  # 使用 % 符號進行模糊匹配
    else:
        # 處理其他欄位的單一條件
        query_conditions.append(f"{column} = %s")
        params.append(value)

# 將條件連接起來，並生成最終查詢語句
query += " AND ".join(query_conditions)

with MySQL() as db:
    result = db.query(query, tuple(params))  # 確保 params 被傳遞為 tuple

    if result:
        for row in result:
            print(row)
        
        # 將查詢結果保存為 JSON 檔案
        save_to_json(result, "query_result.json")
    else:
        print("查無資料")