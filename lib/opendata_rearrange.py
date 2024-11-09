import os
import shutil
"""
請先下載opendata的資源至opendata資料夾，或根據需求更改路徑
此程式功能為創建一個新資料夾，裡面包含來自opendata的指定data數據，以字母A-Z分類
只選取CSV檔
"""


# Folder name
keywords_to_folders = {
    "C": "c_lvr_land",
    "A": "a_lvr_land",
    "F": "f_lvr_land",
    "H": "h_lvr_land",
    "O": "o_lvr_land",
    "J": "j_lvr_land",
    "K": "k_lvr_land",
    "B": "b_lvr_land",
    "M": "m_lvr_land",
    "N": "n_lvr_land",
    "P": "p_lvr_land",
    "I": "i_lvr_land",
    "Q": "q_lvr_land",
    "D": "d_lvr_land",
    "E": "e_lvr_land",
    "T": "t_lvr_land",
    "G": "g_lvr_land",
    "U": "u_lvr_land",
    "V": "v_lvr_land",
    "X": "x_lvr_land",
    "W": "w_lvr_land",
    "Z": "z_lvr_land"
}

abs_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(abs_file_path)

# 資料夾創建路徑
outputDir = f"{current_dir_path}\\..\\rearrange_data"

if not os.path.exists(outputDir):
    os.makedirs(outputDir)


# 創建A-Z資料夾
for folder in keywords_to_folders.values():
    os.makedirs(os.path.join(outputDir, folder), exist_ok=True)

# 創建未分類資料夾
uncategorized_folder = os.path.join(
    outputDir, "Uncategorized")
if not os.path.exists(uncategorized_folder):
    os.makedirs(uncategorized_folder, exist_ok=True)

for num in range(55):
    directory_to_organize = f"{current_dir_path}\\..\\opendata\\data{num}"
    # 過濾A-Z資料(僅限CSV檔案)
    for filename in os.listdir(directory_to_organize):
        file_path = os.path.join(directory_to_organize, filename)
        move = False
        try:
            if filename.endswith(".csv"):
                for file in keywords_to_folders.values():
                    if file in filename:
                        shutil.move(file_path, os.path.join(
                            outputDir, file, filename))
                        move = True
                        break
                if not move:
                    shutil.move(file_path, os.path.join(
                        uncategorized_folder, filename))
        except Exception as e:
            print(f"發生錯誤{e}")
