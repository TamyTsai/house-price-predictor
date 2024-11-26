import mysql.connector

try:
    conn = mysql.connector.connect(
        host="162.241.253.231",
        user="omeiliau_nou",
        password="Nou@8089",
        database="omeiliau_nou",
        use_pure=True       # 避免使用C擴展
    )
    print("連線成功")
except mysql.connector.Error as err:
    print(f"錯誤: {err}")
