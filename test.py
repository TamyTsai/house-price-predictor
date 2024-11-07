# [I/O]輸入資料表
user_input_list = {
    "city":"",                  # str : 縣市
    "town":"",                  # str : 鄉鎮市區
    "ptype":"",                 # list :  房地、建物、土地、車位
    "p_build":"",               # str : 門牌地址
    "p_startY":"",              # int : 交易期間（年起）101-113
    "p_startM":"",              # int : 交易期間（月起）1-12 
    "p_endY":"",                # int : 交易期間（年迄）101-113
    "p_endM":"",                # int : 交易期間（月迄）1-12 
    "pmoney_unit":"",           # int : 單位（1 => 萬元 , 2 => 元）
    "minp":"",                  # int : 最小值(單價)
    "maxp":"",                  # int : 最大值（單價）
    "unit":"",                  # int : 面積單位（1 => M^2 ，2 => 坪）
    "mins":"",                  # int : 最小值（坪數）
    "maxs":"",                  # int : 最大值（坪數）
    "avg_var":"",               # int : 屋齡

    # 計算部分 (我們自訂的)
    "calculate_Y":"",           # int : 目標期間（年）
    "calculate_M":"",           # int : 目標期間（月）
    "calculate_unit":"",        # int : 面積單位（1 => M^2 ，2 => 坪）
    "calculate_area":""         # int : 面積
}