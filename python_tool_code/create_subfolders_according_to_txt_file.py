import os

def create_subfolders(parent_folder, txt_file):
    with open(txt_file, 'r') as f:
        for line in f:
            subfolder_name = line.strip()
            subfolder_path = os.path.join(parent_folder, subfolder_name)
            os.makedirs(subfolder_path, exist_ok=True)

# 使用方法
create_subfolders('C:/Users/song_/Desktop/ChengyangSong_0805_frames', 'C:/Users/song_/Desktop/ChengyangSong_0805_frames.txt')