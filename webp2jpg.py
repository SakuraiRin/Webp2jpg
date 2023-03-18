import os
import glob
import tkinter as tk
import tkinter.filedialog
from PIL import Image

webp_list = []
#作品フォルダ作成
work_name = input("作品名を入力してください：")
#file_storage_name = input("作品名を入力してください：")

#webpの入っているフォルダの選択
dir = "C:\\"
fld = tk.filedialog.askdirectory(initialdir = dir)
#選択したフォルダの直下に"file_storage_name"フォルダの作成
os.mkdir(os.path.join(fld, work_name))
basename = os.path.basename(work_name)
dir_storage = os.path.join(fld, basename)

#webp_listに"webp"ファイルのパスを投げる
for i in glob.glob(os.path.join(fld, "*.webp")):
    webp_list.append(i)

#"webp"ファイルをjpgに変換して保存
for j in webp_list:
    new_image = Image.open(j).convert("RGB")
    new_path = j.replace(".webp",".jpg")
    
    basename = os.path.basename(new_path)
    new_image.save(os.path.join(dir_storage, basename),quality=95)
#"webp"ファイルの削除
    os.remove(j)