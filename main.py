import GUI

def main():
    print("程式結束")
    # 匯出命令(無控制台)
    # pyinstaller --onefile --name "房價預測器 Windows v0.2.1" --noconsole --hidden-import=mysql.connector.plugins.mysql_native_password <your_script.py>
    
    # 匯出命令(有控制台)
    # pyinstaller --onefile --name "房價預測器 Windows v0.2.1" --hidden-import=mysql.connector.plugins.mysql_native_password <your_script.py>

    # <your_script.py> 填入完整路徑，例如: "C:\Users\陳銘泓\Desktop\GitHub\NOU_python_zzz002_work\main.py"
    # --name "房價預測器 Windows v0.X" 用於設置匯出後檔名，建議: "房價預測器 OS系統 版本號"

main()