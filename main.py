import GUI

def main():
    print("程式結束")
    # 匯出命令(無控制台)
    # pyinstaller --onefile --noconsole --hidden-import=mysql.connector.plugins.mysql_native_password <your_script.py>
    
    # 匯出命令(有控制台)
    # pyinstaller --onefile --hidden-import=mysql.connector.plugins.mysql_native_password <your_script.py>

main()