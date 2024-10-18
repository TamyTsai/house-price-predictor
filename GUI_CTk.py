
# libraries Import
from tkinter import *
import customtkinter

# Main Window Properties

window = Tk()
window.title("Tkinter")
window.geometry("600x800")
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
    font=("Arial", 20),
    text_color="#000000",
    height=40,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Title_1.place(x=50, y=0)

# 註解 1
Title_1_info = customtkinter.CTkLabel(
    master=window,
    text="填寫說明: 輸入之條件建議盡量與目標購置之房屋條件相近，以增加預測可參考性",
    font=("Arial", 14),
    text_color="#646464",
    height=30,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Title_1_info.place(x=10, y=40)

# 底色框 1 ======================================================================= 位置
background_frame_1 = customtkinter.CTkFrame(
    master=window,
    height=80,
    width=550,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8"
)
background_frame_1.place(x=20, y=110)

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
    font=("Arial", 14),
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
Class_2_background = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=550,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Class_2_background.place(x=20, y=210)

# Class_2_title
Class_2_title = customtkinter.CTkLabel(
    master=window,
    text="交易期間:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=80,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Class_2_title.place(x=20, y=220)

# 起始年
Class_2_optionMenu_year1 = customtkinter.CTkOptionMenu(
    master=window,
    values=["100年", "101年", "102年"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=60,
    corner_radius=6,
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Class_2_optionMenu_year1.place(x=120, y=220)

# Class_2_label_1
Class_2_label_1 = customtkinter.CTkLabel(
    master=window,
    text="年",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Class_2_label_1.place(x=180, y=220)

# 起始月
Class_2_optionMenu_mon1 = customtkinter.CTkOptionMenu(
    master=window,
    values=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月" ],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=60,
    corner_radius=6,
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Class_2_optionMenu_mon1.place(x=210, y=220)

# Class_2_label_2
Class_2_label_2 = customtkinter.CTkLabel(
    master=window,
    text="至",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Class_2_label_2.place(x=290, y=220)

# 結束年
Class_2_optionMenu_year2 = customtkinter.CTkOptionMenu(
    master=window,
    values=["100年", "101年", "102年"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=60,
    corner_radius=6,
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Class_2_optionMenu_year2.place(x=340, y=220)

# Class_2_label_3
Class_2_label_3 = customtkinter.CTkLabel(
    master=window,
    text="年",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Class_2_label_3.place(x=400, y=220)

# 結束月
Class_2_optionMenu_mon2 = customtkinter.CTkOptionMenu(
    master=window,
    values=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月" ],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=60,
    corner_radius=6,
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Class_2_optionMenu_mon2.place(x=430, y=220)

# Class_2_label_4
Class_2_label_4 = customtkinter.CTkLabel(
    master=window,
    text="止",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Class_2_label_4.place(x=510, y=220)

# Class_2_title_info
Class_2_title_info = customtkinter.CTkLabel(
    master=window,
    text="說明2",
    font=("Arial", 14),
    text_color="#646464",
    height=30,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Class_2_title_info.place(x=20, y=260)

# 底色框 3 ======================================================================= 單價
Class_3_background = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=360,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Class_3_background.place(x=20, y=300)

# Class_3_title 單價
Class_3_title = customtkinter.CTkLabel(
    master=window,
    text="單價:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Class_3_title.place(x=20, y=330)

# Class_3_radioButton 萬元
Class_3_radioButton_1 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var_price,
    value=25,
    text="萬元",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
Class_3_radioButton_1.place(x=90, y=320)

# Class_3_radioButton 元
Class_3_radioButton_2 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var_price,
    value=26,
    text="元",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
Class_3_radioButton_2.place(x=90, y=350)

# Class_3_entry 最小
Class_3_entry_1 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="最小",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Class_3_entry_1.place(x=170, y=330)

# Class_3_label
Class_3_label = customtkinter.CTkLabel(
    master=window,
    text="~",
    font=("Arial", 16),
    text_color="#000000",
    height=30,
    width=25,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Class_3_label.place(x=260, y=330)

# Class_3_entry 最大
Class_3_entry_2 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="最大",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Class_3_entry_2.place(x=290, y=330)

# 底色框 4 ======================================================================= 面積
Class_4_background = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=360,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Class_4_background.place(x=20, y=390)

# Class_4_title 面積
Class_4_title = customtkinter.CTkLabel(
    master=window,
    text="面積:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Class_4_title.place(x=20, y=400)

# Class_4_radioButton 平方米 M^2
Class_4_radioButton_1 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var_areaA,
    value=34,
    text="平方米",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
Class_4_radioButton_1.place(x=90, y=390)

# Class_4_radioButton 坪
Class_4_radioButton_2 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var_areaA,
    value=36,
    text="坪",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
Class_4_radioButton_2.place(x=90, y=420)

# Class_4_entry 最小
Class_4_entry_1 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="最小",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Class_4_entry_1.place(x=170, y=400)

# Class_4_label
Class_4_label = customtkinter.CTkLabel(
    master=window,
    text="~",
    font=("Arial", 16),
    text_color="#000000",
    height=30,
    width=25,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Class_4_label.place(x=260, y=400)

# Class_4_entry 最大
Class_4_entry_2 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="最大",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Class_4_entry_2.place(x=290, y=400)

# 底色框 5 ======================================================================= 屋齡
Class_5_background = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=200,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Class_5_background.place(x=390, y=340)

# Class_5_title
Class_5_title = customtkinter.CTkLabel(
    master=window,
    text="屋齡:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Class_5_title.place(x=400, y=360)

# 屋齡-選單
Class_5_optionMenu = customtkinter.CTkOptionMenu(
    master=window,
    values=["1年內", "1~3年", "3~5年", "5~10年", "10~20年", "20年以上"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=80,
    corner_radius=6,
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Class_5_optionMenu.place(x=470, y=360)


# 大標 2 ======================================================================= 目標
Title_2 = customtkinter.CTkLabel(
    master=window,
    text="目標購置之房屋資訊",
    font=("Arial", 20),
    text_color="#000000",
    height=40,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Title_2.place(x=0, y=470)


# 底色框 6 ======================================================================= 目標時間
Class_6_background = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=60,
    width=350,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Class_6_background.place(x=20, y=510)

# Class_6_title
Class_6_title = customtkinter.CTkLabel(
    master=window,
    text="時間:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Class_6_title.place(x=20, y=520)

# 目標時間 年
Class_6_optionMenu_year = customtkinter.CTkOptionMenu(
    master=window,
    values=["100年", "101年", "102年"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=80,
    corner_radius=6,
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Class_6_optionMenu_year.place(x=110, y=520)

# Class_6_label_1
Class_6_label_1 = customtkinter.CTkLabel(
    master=window,
    text="~",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Class_6_label_1.place(x=200, y=520)

# 目標時間 月
Class_6_optionMenu_mon = customtkinter.CTkOptionMenu(
    master=window,
    values=["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月" ],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=40,
    width=80,
    corner_radius=6,
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Class_6_optionMenu_mon.place(x=240, y=520)

# 底色框 7 ======================================================================= 目標面積
Class_7_background = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=350,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Class_7_background.place(x=20, y=580)

# Class_7_title
Class_7_title = customtkinter.CTkLabel(
    master=window,
    text="面積:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Class_7_title.place(x=20, y=590)

# 選項-M^2
Class_7_radioButton_1 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var_areaB,
    value=45,
    text="平方米",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
Class_7_radioButton_1.place(x=100, y=580)

# 選項-坪
Class_7_radioButton_2 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var_areaB,
    value=46,
    text="坪",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
Class_7_radioButton_2.place(x=100, y=610)

# 輸入面積
Class_7_entry = customtkinter.CTkEntry(
    master=window,
    placeholder_text="輸入面積",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=40,
    width=120,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Class_7_entry.place(x=200, y=590)

"""
 ########################################  資料輸出區  ########################################
"""

# 生成資料按鈕
Output_button = customtkinter.CTkButton(
    master=window,
    text="生成資料",
    font=("undefined", 18),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=50,
    width=150,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#75f6ff",
    )
Output_button.place(x=200, y=660)

# 輸出區
Output_label = customtkinter.CTkLabel(
    master=window,
    text="輸出區",
    font=("Arial", 16),
    text_color="#0033ff",
    height=80,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Output_label.place(x=140, y=720)

#run the main loop
window.mainloop()

