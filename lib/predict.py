import pandas as pd
import numpy as np

# 抓下來是字串 單價要轉為數字後再收下來
original_trade_time = [113/09/24, 113/09/24, 113/09/14, 113/08/25, 113/08/15, 113/06/02, 112/11/11, 112/11/08, 111/06/05] # 交易時間 原始爬蟲資料範例(內政部實價登錄平台中，交易資料預設排設依據為交易日期，由新至舊)
original_house_price_per_pin = [27.1, 28.6, 26.2, 24.6, 23.1, 23.1, 20.5, 20.8, 19] # 單價 原始爬蟲資料範例(如果是單價是每平方公尺的價格，則要先經過轉換)

# 按月計算每坪單價之平均
# 將original_trade_time及original_house_price_per_pin串列元素做前後反轉(讓資料都由舊排至新)
trade_time_order = [111/06/05, 112/11/08, 112/11/11, 113/06/02, 113/08/15, 113/08/25, 113/09/14, 113/09/24, 113/09/24]
house_price_per_pin_order = [19, 20.8, 20.5, 23.1, 23.1, 24.6, 26.2, 28.6, 27.1]
# 抓出original_trade_time_order串列中，相同月份的元素的索引值，以該索引值抓出original_house_price_per_pin_order串列中同一月份的單價
# 計算同一月份的單價之平均，依月份舊到新指定給新串列house_price_per_pin_month_average
house_price_per_pin_month_average = [19, 20.65, 23.1, 23.85, 27.3]

# 交易時間資料按月形成新串列
# 取trade_time_order串列元素之年月資料，不取日資料
# 將同一年月資料視為一筆（一個元素） 形成新串列
trade_time_month = [111/06, 112/11, 112/11, 113/06, 113/08, 113/08, 113/09, 113/09, 113/09]

# 交易時間資料處理成解釋變數
# 以串列中第一個元素為基準，計算其他元素應轉換之值
trade_time = [0, 17, 17 ,24, 26, 26, 27, 27, 27]


buy_date = 29 # 使用者輸入的購置時間 並經過轉換
buy_pin = 36.5 # 使用者輸入的標的坪數（如為平方公尺 要先經過轉換）

data = pd.DataFrame({'X': trade_time, 'Y': house_price_per_pin_month_average})
# pd.DataFrame(字典資料)

cofficients = np.polyfit(data['X'], data['Y'], 1)
# 使用numpy的polyfit函數 進行 最小平方法擬合
# 1 表示擬合 「一次」多項式模型（直線）
# np.polyfit(字典[對應自變數的key], 字典[對應應變數的key], 想要擬合幾次多項式)
# cofficients = [斜率, 截距]

slope = cofficients[0]
intercept = cofficients[1]

# 預測單坪價格公式
predicted_house_price_per_pin = intercept + slope * buy_date

# 預測房屋總價
predicted_house_total_price = buy_pin * predicted_house_price_per_pin