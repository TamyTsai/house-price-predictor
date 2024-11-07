# NOU_python_zzz002_work
空大113上Pythont程式設計期末小組專案
專案用途與說明 TODO，
<a href="https://nou.tronclass.com.tw/course/54317/group-set#/topics/66121?show_sidebar=false&scrollTo=topic-66121&groupId=9086&pageIndex=1&pageCount=1&topicIds=66121,65692&predicate=lastUpdatedDate&reverse">當前提案（房價預測器）</a>

### 分支管理
採用<a href="https://gitbook.tw/chapters/gitflow/why-need-git-flow">gitflow</a>管理方式，主要目的在開發階段採用分支來進行個人的執行事項．待完成後再合併回developer分支，最終穩定版本使用main分支，git UI介面可以使用 <a href="https://www.sourcetreeapp.com/">sourcetree</a>

<a href="https://gitbook.tw/chapters/gitflow/using-git-flow">在sourcetree使用git flow</a>

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
GUI 介面 Mark
房價預測模型 婷羽
過濾數據（資料庫select相關語句）惠婷
數據與處理（csv檔案彙整成要寫入資料庫格式）2魚
資料庫連接與封裝方法 秉蒼
報告簡報 Cindy
報告 Cindy
程式測試
程式文件

### 資料結構與用途說明
```
README.md           專案說明與注意事項，使用markdown寫法
main.py             應用程式執行入口點
index.html          網站首頁
scripts/            網頁前端功能
    script.js       網頁前端功能
stylesheets/        css樣式
    application.css 整個網站共用的樣式   
lib/                各種類別的程式
    Api.py          提供HTTP呼叫API的快速方法
```

### 資料庫相關
資料庫主機：162.241.253.231
資料庫port：3306
資料庫名稱： omeiliau_nou

### 資料表與結構
| csv檔案中的欄位名稱 | 資料庫欄位名稱 | 資料型別 | 預設值 | 備註                                |
|------------------|--------------|---------|-------|------------------------------------|
|                  | city_code    | string  |       | 縣市代號 （參照params.py的city字典Key）|
|                  | city_name    | string  |       | 縣市名稱 （參照params.py的city字典Key）|
|                  | town_code    | string  |       | 鄉鎮市區參照params.py的city字典key）   |
| 鄉鎮市區          | town_name    | string   |       | 鄉鎮市區參照params.py的city字典value   |
| 交易標地          |trade_sign    | int      |       |（房地 => 1 建物 => 2 土地=> 3 車位=>4, 房地+車位 => 5）|
|土地位置建物門牌    |address        |strnig    |      |                                     |
|交易年月日          | trade_date   | int      |       |                                    |
|成交總價(元)        |price_total   | int      |      |                                     |
|單價元平方公尺       | price_nuit   | int      |     |                                      |
|建物移轉總面積平方公尺| total_area   | float     |     |                                     |
| 編號              | code         | string    |     |                                     |
| 屋齡              | age          | int       |  0  | 此處比較特特別，假測現在開啟的檔案是a_lvr_land_a.csv要取這份檔案中的「編號」欄位的值，然後到a_lvr_land_a_build.csv這份檔案對應的「編號」取得屋齡，如果是土地就沒有屋齡問題預設值為0|