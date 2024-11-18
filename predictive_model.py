import pandas as pd
import numpy as np
import json

# 預測函式
# 根據使用者輸入，呼叫撈取資料庫對應資料之函式，運用迴歸公式，產出預測單價（萬元/坪），供GUI呼叫並計算（單價*目標面積（坪）=預測總價（萬元））以顯示預測結果
def input_io_call(user_input_list):
    # 以使用者查詢輸入作為參數，呼叫撈取資料庫資料函式
    # 獲取「交易年月」及「各交易年月平均單價」（json檔：key為交易年月，value為該月平均單價（元/平方公尺））（資料按交易時間由舊到新排序），並將回傳的結果儲存到變數origin_data
    # json檔範例：
    # {
    #     11110: 116730, # 111年10月之平均成交價為每平方公尺116730元
    #     11205: 121716,
    #     11307: 124736
    # }

    # 將json檔的key交易年月轉成串列，儲存到變數trade_time_month
    trade_time_month = list(origin_data.keys()) # 使用 .keys() 方法獲取json檔中所有 key，並轉成串列
    # 範例：trade_time_month = [11110, 11205, 11307]

    # 將json檔的value各月平均單價（元/平方公尺）轉成串列，儲存到變數house_price_per_square_meter_month_average
    house_price_per_square_meter_month_average = list(origin_data.values())
    # 範例：house_price_per_square_meter_month_average = [116730, 121716, 124736]

    # 轉換變數trade_time_month的元素（交易年月）（最早的交易年月為0，其餘以此類推），儲存為變數trade_time
    # 將串列中第一個元素作為基期年月（因為資料庫在挑資料時已經按交易時間由舊到新排序，所以列表中第一個元素為交易時間最早的資料）
    base_year = trade_time_month[0] // 100 # 提取基期年份
    # 範例：base_year = 111（年）
    base_month = trade_time_month[0] % 100 # 提取基期月份
    # 範例：11110%100 = 10（月）
    # 範例：base_month = 10
    # 計算串列中每個元素與基期的月份差距
    trade_time = [] # 先創建交易年月轉換結果的空串列，等下再用迴圈把轉換後結果一一加進本串列
    for year_month in trade_time_month: # year_month指串列trade_time_month中每個單一元素（如：11110）
        year = year_month // 100 # 提取年份
        month = year_month % 100 # 提取月份
        # 差一年代表差12個月，計算年份差與月份差，以得到月份差距
        month_difference = (year - base_year) * 12 + (month - base_month)
        trade_time.append(month_difference)
    # 範例：trade_time = [0, 7, 21]
    # （111年10月與基期111年10月相差0個月；112年5月與111年10月相差7個月；113年7月與111年10月相差21個月）

    # 取得使用者輸入的欲購置交易年月，並儲存為變數buy_time_year與buy_time_month
    buy_time_year = user_input_list[calculate_Y] # 從使用者輸入字典中提取key為calculate_Y所對應之value（目標期間（年））
    # 範例：buy_time_year = 114
    buy_time_month = user_input_list[calculate_M] # 從使用者輸入字典中提取key為calculate_M所對應之value（目標期間（月））
    # 範例：buy_time_month = 3

    # 轉換變數buy_time_year與buy_time_month，並儲存為變數buy_time
    buy_time = (buy_time_year - base_year) * 12 + (buy_time_month - base_month)
    # 範例：buy_time = 29
    # （欲購置時間114年3月與基期111年10月相差29個月）

    # 產生預測公式（最小平方迴歸法擬合）
    data = pd.DataFrame({'X': trade_time, 'Y': house_price_per_square_meter_month_average})
    # pd.DataFrame(字典資料)
    # 範例：trade_time = [0, 7, 21]
    # 範例：house_price_per_square_meter_month_average = [116730, 121716, 124736]

    cofficients = np.polyfit(data['X'], data['Y'], 1)
    # 使用numpy的polyfit函式 進行 最小平方法擬合
    # 1 表示擬合 「一次」多項式模型（直線）
    # np.polyfit(字典[對應自變數的key], 字典[對應應變數的key], 想要擬合幾次多項式)
    # cofficients = [斜率, 截距]

    slope = cofficients[0] # 斜率
    intercept = cofficients[1] # 截距

    # 預測單價（元/平方公尺）公式
    predicted_house_price_per_square_meter = intercept + slope * buy_time
    # 轉換為單價之單位為「萬元/坪」
    predicted_house_price_per_pin = predicted_house_price_per_square_meter / 10000 / 0.3025

    # 回傳預測單價（萬元/坪）
    return predicted_house_price_per_pin
    # 範例：42.34489458593352（萬元/坪）
    



