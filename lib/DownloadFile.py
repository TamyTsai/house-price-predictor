import os
import requests
from datetime import datetime
import zipfile

'''
open data 下載規則與邏輯

最近資料下載位置 https://plvr.land.moi.gov.tw//Download?type=zip&fileName=lvr_landcsv.zip

前一期資料 下載下來的資料會有csv txt xml檔案同時存在
https://plvr.land.moi.gov.tw/DownloadHistory?type=history&fileName=20241001
https://plvr.land.moi.gov.tw/DownloadHistory?type=history&fileName=20241011
https://plvr.land.moi.gov.tw/DownloadHistory?type=history&fileName=20241021

season 季度資料
規則由101S1開始到113S4
https://plvr.land.moi.gov.tw//DownloadSeason?season=113S3&type=zip&fileName=lvr_landcsv.zip

檔案規則
範例 a_lvr_land_a_build.csv
第一區塊：檔案開頭的英文字代表區域 a 表示台北對照表請見lib/params.py中的city字典
第二區塊：lvr 固定字串
第三區塊：land固定字串
第四區塊：a b都是買賣資料 c為租賃資料，目前還不清楚ab的差異
第五區塊：land表示土地 build表示建物 park 表示車位
'''

def getSeason():
    '''
    取得從101年到當前的年+季
    Return:
        list 格式為 {年份}S{第幾季}
    '''
    # 取現在的西元年轉換為民國
    current_year = datetime.now().year
    ORGY = current_year - 1911
    #現在的季度
    current_quarter = ((datetime.now().month - 1) // 3) + 1
    items = []
    # 迴圈跑年
    for year in range(101, ORGY+1):
        # 迴圈跑季
        for s in range(1, 5):
            if ORGY == year and s >= current_quarter:
                break
            index = len(items)
            items.append(index)
            items[index] = f"{year}S{s}"
    return items

def downloadFile(file, url, params={}):
    '''
    Args:
        file: (string) 要存放的檔案路徑含檔名
        url: (string) 要下載的檔案位置
        params: (dist) 要串送的參數
    Return:
        bool
    '''
    # 當前程式的路徑
    current_path = os.getcwd()
    # 將資料存在opendata資料夾中
    response = requests.get(url, params)
    if response.status_code == 200:
        with open(file, 'wb') as file:
            # 分塊下載避免資料不完全
            for chunk in response.iter_content(1024):  
                file.write(chunk)
            return True
    else:
        return False

def UnZip(file, output):
    '''
    解壓縮檔案（zip檔）到指定的路徑
    Args:
        file: (string) 要解壓縮的檔案位置
        url: (string) 解壓縮後要輸出的檔案路徑含檔名
    Return:
        bool
    '''
    if not os.path.exists(output):
        os.makedirs(output)
    # 解壓縮 ZIP 檔案
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(output)
    return True


# OPEN DATA 網址
URL = "https://plvr.land.moi.gov.tw"

# 要下載的檔案列表
PARAMS = [
    {"path": "Download", "params":{"type": "zip", "fileName": "lvr_landcsv.zip"}},
    {"path": "DownloadHistory", "params":{"type": "history", "fileName": "20241001"}},
    {"path": "DownloadHistory", "params":{"type": "history", "fileName": "20241011"}},
    {"path": "DownloadHistory", "params":{"type": "history", "fileName": "20241021"}},
]

# 填充要下載的季度路徑
for season in getSeason():
    index = len(PARAMS)
    PARAMS.append(index)
    PARAMS[index] = {"path": "DownloadSeason", "params":{"season": season, "type": "zip", "fileName": "lvr_landcsv.zip"}}

i = 0
# 當前程式的路徑
current_path = os.getcwd()
# 要存放下載檔案的資料夾路徑
outputDir = f"{current_path}/../opendata"
# 檢查資料夾是否存在，不存在則創建
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
# 下載檔案
for item in PARAMS:

    # 測試時只抓一筆就好
    # if(i >= 1):
    #     break
    
    # 壓縮檔名稱
    zipPath = f"{outputDir}/data{i}.zip"

    # 下載檔案，將資料流寫到本地檔案中
    result = downloadFile(zipPath, f"{URL}/{item['path']}", item['params'])

    if result == True:
        print(f"{i}-下載成功")
        # 使用黨名作為資料夾將資料解壓縮
        unzipResult = UnZip(zipPath, zipPath.replace(".zip", ""))
        if unzipResult :
            print(f"{i}-解壓縮完成")
            if os.path.exists(zipPath):
                os.remove(zipPath)
                print(f"{i}-已刪除下載的ZIP檔")
        else:
            print(f"{i}-解壓縮失敗")
    else:
        print(f"{i}-下載失敗")
    i += 1