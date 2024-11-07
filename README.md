# NOU_python_zzz002_work
空大113上Pythont程式設計期末小組專案
專案用途與說明 TODO，
<a href="https://nou.tronclass.com.tw/course/54317/group-set#/topics/66121?show_sidebar=false&scrollTo=topic-66121&groupId=9086&pageIndex=1&pageCount=1&topicIds=66121,65692&predicate=lastUpdatedDate&reverse">當前提案（房價預測器）</a>

### 分支管理
採用<a href="https://gitbook.tw/chapters/gitflow/why-need-git-flow">gitflow</a>管理方式，主要目的在開發階段採用分支來進行個人的執行事項．待完成後再合併回developer分支，最終穩定版本使用main分支，git UI介面可以使用 <a href="https://www.sourcetreeapp.com/">sourcetree</a>

### 分支 GUI
by Mark ;
套件: tkinter、customtkinter ;
進度: 基本排版/字型/樣式、淺色/深色模式樣式適應+切換按鈕 ;
待辦: 事件系統(進行中)、跨平台適應
*
11/08
事件系統: 年/月 選擇部分皆已完成
-
增加 user_input_list 字典，用於存放使用者輸入
-
增加 user_input_list {
"calculate_Y":"",           # int : 目標期間（年）
"calculate_M":"",           # int : 目標期間（月）
"calculate_unit":"",        # int : 面積單位（1 => M^2 ，2 => 坪）
"calculate_area":""         # int : 面積
}
用於存放計算目標變數
-
增加 target_year_dict 計算目標(年) 的選單 (我只抓10年)

### 運行環境與依賴套件
```
python 3.x.x    最新穩定版本(當前3.12.7)
pip3            最新穩定隨付(當前24.2)
request         進行http的訪問與資料取得
Beautifulsoup4  網路爬蟲取得的資料解析
tkinter         UI介面處理(未定)
```

### 註解格式
依循 PEP 257
``` python
def add(a, b):
    """
    Return the sum of two numbers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int, float: The sum of the two numbers.

    Example:
        >>> add(3, 4)
        7
        >>> add(10.5, 5.5)
        16.0
        return a + b
    """

    return a + b
```

### 流程圖
TODO

### 工作分派與負責
TODO

### 資料結構與用途說明
```
README.md           專案說明與注意事項，使用markdown寫法
main.py             應用程式執行入口點
lib/                各種類別的程式
    Api.py          提供HTTP呼叫API的快速方法
```
