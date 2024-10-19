
# libraries Import
from tkinter import *
import customtkinter

# Main Window Properties

window = Tk()
window.title("Tkinter")
window.geometry("600x720")
window.configure(bg="#FFFFFF")


radio_var_price = IntVar()
radio_var_areaA = IntVar()
radio_var_areaB = IntVar()

"""
 ########################################  版面配置區  ########################################
"""

# 大標 1
Title_1 = customtkinter.CTkLabel(
    master=window,
    text="欲統計分析之交易資料條件範圍",
    font=("Microsoft JhengHei", 20, "bold"),
    anchor="w",  # 左對齊
    text_color="#000000",
    height=40,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Title_1.place(x=10, y=0)

# 註解 1
Title_1_info = customtkinter.CTkLabel(
    master=window,
    text="填寫說明: 輸入之條件建議盡量與目標購置之房屋條件相近，以增加預測可參考性",
    font=("Microsoft JhengHei", 14),
    anchor="w",
    text_color="#646464",
    height=30,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Title_1_info.place(x=10, y=30)

# 底色框 1 ======================================================================= 位置
background_frame_1 = customtkinter.CTkFrame(
    master=window,
    height=80,
    width=550,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8"
)
background_frame_1.place(x=20, y=60)

# 選單-縣市
Class_1_optionMenu_1 = customtkinter.CTkOptionMenu(
    master=background_frame_1,
    values=["選項1", "選項2", "選項3"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=50,
    width=60,
    corner_radius=8,
    bg_color="transparent",
    fg_color="#F0F0F0",
)
Class_1_optionMenu_1.place(x=10, y=15)

# 選單-鄉鎮市區
Class_1_optionMenu_2 = customtkinter.CTkOptionMenu(
    master=background_frame_1,
    values=["選項1", "選項2", "選項3"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=50,
    width=95,
    corner_radius=8,
    bg_color="transparent",
    fg_color="#F0F0F0",
)
Class_1_optionMenu_2.place(x=120, y=15)

# Class_1_checkbox 房屋
Class_1_checkbox_1 = customtkinter.CTkCheckBox(
    master=background_frame_1,
    text="房屋",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    height=30,
    width=60,
)
Class_1_checkbox_1.place(x=280, y=10)

# Class_1_checkbox 土地
Class_1_checkbox_2 = customtkinter.CTkCheckBox(
    master=background_frame_1,
    text="土地",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    height=30,
    width=60,
)
Class_1_checkbox_2.place(x=280, y=40)

# Class_1_checkbox 建物
Class_1_checkbox_3 = customtkinter.CTkCheckBox(
    master=background_frame_1,
    text="建物",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    height=30,
    width=60,
)
Class_1_checkbox_3.place(x=350, y=10)

# Class_1_checkbox 車位
Class_1_checkbox_4 = customtkinter.CTkCheckBox(
    master=background_frame_1,
    text="車位",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    height=30,
    width=60,
)
Class_1_checkbox_4.place(x=350, y=40)

# Class_1_entry 門牌/社區名稱
Class_1_entry = customtkinter.CTkEntry(
    master=background_frame_1,
    placeholder_text="門牌/社區名稱",
    placeholder_text_color="#454545",
    font=("Microsoft JhengHei", 14),
    text_color="#000000",
    height=50,
    width=120,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="transparent",
    fg_color="#F0F0F0",
)
Class_1_entry.place(x=420, y=15)


# 底色框 2 ======================================================================= 時間
background_frame_2 = customtkinter.CTkFrame(
    master=window,
    height=80,
    width=550,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8"
)
background_frame_2.place(x=20, y=160)

# Class_2_title
Class_2_title = customtkinter.CTkLabel(
    master=background_frame_2,
    text="交易期間:",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=80,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
)
Class_2_title.place(x=5, y=15)

# 起始年
Class_2_optionMenu_year1 = customtkinter.CTkOptionMenu(
    master=background_frame_2,
    values=["100年", "101年", "102年"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=60,
    corner_radius=6,
    bg_color="transparent",
    fg_color="#F0F0F0",
)
Class_2_optionMenu_year1.place(x=90, y=15)

# Class_2_label_1
Class_2_label_1 = customtkinter.CTkLabel(
    master=background_frame_2,
    text="年",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=20,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
)
Class_2_label_1.place(x=180, y=15)

# 起始月
Class_2_optionMenu_mon1 = customtkinter.CTkOptionMenu(
    master=background_frame_2,
    values=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月" ],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=60,
    corner_radius=6,
    bg_color="transparent",
    fg_color="#F0F0F0",
)
Class_2_optionMenu_mon1.place(x=200, y=15)

# Class_2_label_2
Class_2_label_2 = customtkinter.CTkLabel(
    master=background_frame_2,
    text="至",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=20,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
)
Class_2_label_2.place(x=280, y=15)

# 結束年
Class_2_optionMenu_year2 = customtkinter.CTkOptionMenu(
    master=background_frame_2,
    values=["100年", "101年", "102年"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=60,
    corner_radius=6,
    bg_color="transparent",
    fg_color="#F0F0F0",
)
Class_2_optionMenu_year2.place(x=310, y=15)

# Class_2_label_3
Class_2_label_3 = customtkinter.CTkLabel(
    master=background_frame_2,
    text="年",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=20,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
)
Class_2_label_3.place(x=400, y=15)

# 結束月
Class_2_optionMenu_mon2 = customtkinter.CTkOptionMenu(
    master=background_frame_2,
    values=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月" ],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=60,
    corner_radius=6,
    bg_color="transparent",
    fg_color="#F0F0F0",
)
Class_2_optionMenu_mon2.place(x=430, y=15)

# Class_2_label_4
Class_2_label_4 = customtkinter.CTkLabel(
    master=background_frame_2,
    text="止",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=20,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
)
Class_2_label_4.place(x=520, y=15)

# Class_2_title_info
Class_2_title_info = customtkinter.CTkLabel(
    master=background_frame_2,
    text="填寫說明: 建議選擇欲購置時間的前半年至一年左右",
    font=("Microsoft JhengHei", 14),
    anchor="w",
    text_color="#646464",
    height=20,
    width=300,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
)
Class_2_title_info.place(x=10, y=57)

# 底色框 3 ======================================================================= 單價
background_frame_3 = customtkinter.CTkFrame(
    master=window,
    height=60,
    width=360,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8"
)
background_frame_3.place(x=20, y=250)

# Class_3_title 單價
Class_3_title = customtkinter.CTkLabel(
    master=background_frame_3,
    text="單價:",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
    )
Class_3_title.place(x=5, y=10)

# Class_3_radioButton 萬元
Class_3_radioButton_1 = customtkinter.CTkRadioButton(
    master=background_frame_3,
    variable=radio_var_price,
    value=10000,
    text="萬元",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=20,
    width=40,
    )
Class_3_radioButton_1.place(x=70, y=5)

# Class_3_radioButton 元
Class_3_radioButton_2 = customtkinter.CTkRadioButton(
    master=background_frame_3,
    variable=radio_var_price,
    value=1,
    text="元",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=20,
    width=40,
    )
Class_3_radioButton_2.place(x=70, y=35)

# Class_3_entry 最小
Class_3_entry_1 = customtkinter.CTkEntry(
    master=background_frame_3,
    placeholder_text="最小",
    placeholder_text_color="#454545",
    font=("Microsoft JhengHei", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="transparent",
    fg_color="#F0F0F0",
    )
Class_3_entry_1.place(x=150, y=15)

# Class_3_label
Class_3_label = customtkinter.CTkLabel(
    master=background_frame_3,
    text="~",
    font=("Microsoft JhengHei", 18),
    text_color="#000000",
    height=30,
    width=25,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
    )
Class_3_label.place(x=240, y=15)

# Class_3_entry 最大
Class_3_entry_2 = customtkinter.CTkEntry(
    master=background_frame_3,
    placeholder_text="最大",
    placeholder_text_color="#454545",
    font=("Microsoft JhengHei", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="transparent",
    fg_color="#F0F0F0",
    )
Class_3_entry_2.place(x=270, y=15)

# 底色框 4 ======================================================================= 面積
background_frame_4 = customtkinter.CTkFrame(
    master=window,
    height=60,
    width=360,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8"
)
background_frame_4.place(x=20, y=320)

# Class_4_title 面積
Class_4_title = customtkinter.CTkLabel(
    master=background_frame_4,
    text="面積:",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
    )
Class_4_title.place(x=5, y=10)

# Class_4_radioButton 平方米 M^2
Class_4_radioButton_1 = customtkinter.CTkRadioButton(
    master=background_frame_4,
    variable=radio_var_areaA,
    value=0,
    text="平方米",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=20,
    width=60,
    )
Class_4_radioButton_1.place(x=70, y=5)

# Class_4_radioButton 坪
Class_4_radioButton_2 = customtkinter.CTkRadioButton(
    master=background_frame_4,
    variable=radio_var_areaA,
    value=1,
    text="坪",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=20,
    width=60,
    )
Class_4_radioButton_2.place(x=70, y=35)

# Class_4_entry 最小
Class_4_entry_1 = customtkinter.CTkEntry(
    master=background_frame_4,
    placeholder_text="最小",
    placeholder_text_color="#454545",
    font=("Microsoft JhengHei", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="transparent",
    fg_color="#F0F0F0",
    )
Class_4_entry_1.place(x=150, y=15)

# Class_4_label
Class_4_label = customtkinter.CTkLabel(
    master=background_frame_4,
    text="~",
    font=("Microsoft JhengHei", 18),
    text_color="#000000",
    height=30,
    width=25,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
    )
Class_4_label.place(x=240, y=15)

# Class_4_entry 最大
Class_4_entry_2 = customtkinter.CTkEntry(
    master=background_frame_4,
    placeholder_text="最大",
    placeholder_text_color="#454545",
    font=("Microsoft JhengHei", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="transparent",
    fg_color="#F0F0F0",
    )
Class_4_entry_2.place(x=270, y=15)

# 底色框 5 ======================================================================= 屋齡
background_frame_5 = customtkinter.CTkFrame(
    master=window,
    height=60,
    width=180,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8"
)
background_frame_5.place(x=390, y=250)

# Class_5_title
Class_5_title = customtkinter.CTkLabel(
    master=background_frame_5,
    text="屋齡:",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
    )
Class_5_title.place(x=10, y=10)

# 屋齡-選單
Class_5_optionMenu = customtkinter.CTkOptionMenu(
    master=background_frame_5,
    values=["1年內", "1~3年", "3~5年", "5~10年", "10~20年", "20年以上"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=80,
    corner_radius=6,
    bg_color="transparent",
    fg_color="#F0F0F0",
    )
Class_5_optionMenu.place(x=70, y=10)


# 大標 2 ======================================================================= 目標
Title_2 = customtkinter.CTkLabel(
    master=window,
    text="目標購置之房屋資訊",
    font=("Microsoft JhengHei", 20, "bold"),
    anchor="w",
    text_color="#000000",
    height=40,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Title_2.place(x=10, y=390)


# 底色框 6 ======================================================================= 目標時間
background_frame_6 = customtkinter.CTkFrame(
    master=window,
    height=60,
    width=350,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8"
)
background_frame_6.place(x=20, y=430)

# Class_6_title
Class_6_title = customtkinter.CTkLabel(
    master=background_frame_6,
    text="時間:",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
    )
Class_6_title.place(x=5, y=10)

# 目標時間 年
Class_6_optionMenu_year = customtkinter.CTkOptionMenu(
    master=background_frame_6,
    values=["100年", "101年", "102年"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=80,
    corner_radius=6,
    bg_color="transparent",
    fg_color="#F0F0F0",
    )
Class_6_optionMenu_year.place(x=90, y=10)

# Class_6_label_1
Class_6_label_1 = customtkinter.CTkLabel(
    master=background_frame_6,
    text="~",
    font=("Microsoft JhengHei", 18),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
    )
Class_6_label_1.place(x=180, y=10)

# 目標時間 月
Class_6_optionMenu_mon = customtkinter.CTkOptionMenu(
    master=background_frame_6,
    values=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月" ],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=80,
    corner_radius=6,
    bg_color="transparent",
    fg_color="#F0F0F0",
    )
Class_6_optionMenu_mon.place(x=220, y=10)

# 底色框 7 ======================================================================= 目標面積
background_frame_7 = customtkinter.CTkFrame(
    master=window,
    height=60,
    width=350,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8"
)
background_frame_7.place(x=20, y=500)

# Class_7_title
Class_7_title = customtkinter.CTkLabel(
    master=background_frame_7,
    text="面積:",
    font=("Microsoft JhengHei", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="transparent",
    fg_color="transparent",
    )
Class_7_title.place(x=5, y=10)

# 選項-M^2
Class_7_radioButton_1 = customtkinter.CTkRadioButton(
    master=background_frame_7,
    variable=radio_var_areaB,
    value=0,
    text="平方米",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=20,
    width=60,
    )
Class_7_radioButton_1.place(x=80, y=5)

# 選項-坪
Class_7_radioButton_2 = customtkinter.CTkRadioButton(
    master=background_frame_7,
    variable=radio_var_areaB,
    value=1,
    text="坪",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=20,
    width=60,
    )
Class_7_radioButton_2.place(x=80, y=35)

# 輸入面積
Class_7_entry = customtkinter.CTkEntry(
    master=background_frame_7,
    placeholder_text="輸入面積",
    placeholder_text_color="#454545",
    font=("Microsoft JhengHei", 14),
    text_color="#000000",
    height=40,
    width=120,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="transparent",
    fg_color="#F0F0F0",
    )
Class_7_entry.place(x=180, y=10)

"""
 ########################################  資料輸出區  ########################################
"""

# 生成資料按鈕
Output_button = customtkinter.CTkButton(
    master=window,
    text="生成資料",
    font=("Microsoft JhengHei", 18, "bold"),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=50,
    width=140,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#75f6ff",
    )
Output_button.place(x=230, y=580)

# 輸出區
Output_label = customtkinter.CTkLabel(
    master=window,
    text="輸出區",
    font=("Microsoft JhengHei", 16),
    text_color="#0033ff",
    height=70,
    width=580,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#EEEEEE",
    )
Output_label.place(x=10, y=640)

#run the main loop
window.mainloop()

