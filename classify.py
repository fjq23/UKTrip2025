import os
import shutil
from datetime import datetime

source_folder = r'D:\CodingNotes\UK2025\pics'

files = os.listdir(source_folder)

for file in files:
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        modification_time = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(modification_time)
        date_folder = date.strftime('%Y-%m-%d')
        target_folder = os.path.join(source_folder, date_folder)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        shutil.move(file_path, os.path.join(target_folder, file))

print("文件分类完成。")

