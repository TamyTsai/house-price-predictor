import mysql.connector
from mysql.connector import Error

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
                database=self.database,
                use_pure=True       # 避免使用C擴展
            )
            if self.connection.is_connected():
                print("成功連接到資料庫")
        except Error as e:
            print(f"連接資料庫失敗: {e}")
            self.connection = None
        except Exception as e:
            print(f"其他異常: {e}")
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

    def delete(self, sql, params=None):
        """
        執行刪除操作並提交變更
        with MySQL() as db:
            db.delete("DELETE FROM lvr_lnd WHERE column = %s", (value,))
        """
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute(sql, params)
                self.connection.commit()
                print(f"刪除了 {cursor.rowcount} 筆資料")
            except Error as e:
                print(f"刪除失敗: {e}")
                self.connection.rollback()
            finally:
                cursor.close()

    def insert(self, sql, params=None):
        """
        執行插入操作並提交變更
        with MySQL() as db:
            db.insert("INSERT INTO lvr_lnd (column1, column2) VALUES (%s, %s)", ("value1", "value2"))
        """
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute(sql, params)
                self.connection.commit()
                print(f"插入了 {cursor.rowcount} 筆資料")
            except Error as e:
                print(f"插入失敗: {e}")
                self.connection.rollback()
            finally:
                cursor.close()
    
    def insert_many(self, sql, params_list):
        """
        執行批次插入操作並提交變更
        with MySQL() as db:
            data_to_insert = [
                ("value1", "value2"),
                ("value3", "value4"),
                ("value5", "value6")
            ]
            db.insert_many("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", data_to_insert)
        """
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.executemany(sql, params_list)
                self.connection.commit()
                print(f"批次插入了 {cursor.rowcount} 筆資料")
            except Error as e:
                print(f"批次插入失敗: {e}")
                self.connection.rollback()
            finally:
                cursor.close()

    def __enter__(self):
        """允許 with 語句使用此類別"""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """結束時自動關閉連線"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("資料庫連線已關閉")