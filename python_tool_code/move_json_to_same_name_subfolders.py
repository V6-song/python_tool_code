import os
import shutil

def move_json_files(src_parent_folder, dst_parent_folder):
    for dirpath, dirnames, filenames in os.walk(src_parent_folder):
        if 'annotations.json' in filenames:
            src_file = os.path.join(dirpath, 'annotations.json')
            dst_dir = os.path.join(dst_parent_folder, os.path.basename(dirpath))
            os.makedirs(dst_dir, exist_ok=True)
            dst_file = os.path.join(dst_dir, 'annotations.json')
            shutil.move(src_file, dst_file)

# 使用方法
# move_json_files('your_src_parent_folder_path', 'your_dst_parent_folder_path')
move_json_files('F:/ChengyangSong_0805_frames', 'C:/Users/song_/Desktop/ChengyangSong_0805_frames')