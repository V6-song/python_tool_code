# import os
# from os.path import isfile, join
# import shutil
#
# def rename_files_in_directory(directory_path):
#     # 获取目录中的所有文件
#     files = [f for f in os.listdir(directory_path) if isfile(join(directory_path, f))]
#
#     # 按照文件的创建时间进行排序
#     files.sort(key=lambda x: os.path.getctime(join(directory_path, x)))
#
#     # 遍历排序后的文件数组，对每个文件进行重命名
#     for i, filename in enumerate(files):
#         old_file_path = join(directory_path, filename)
#         new_file_path = join(directory_path, f"Video_{str(i+401).zfill(4)}{os.path.splitext(filename)[1]}")
#         shutil.move(old_file_path, new_file_path)
#
# rename_files_in_directory('C://Users//song_//Desktop//song_train_dataset')


#对文件夹下面的子文件夹重新命名，从Video_401开始
import os

# 你的文件夹的绝对路径
parent_dir = 'C://Users//song_//Desktop//song_train_dataset'

# 获取所有子文件夹的名称
subdirs = sorted(os.listdir(parent_dir))

# 重新命名每个子文件夹
for i, subdir in enumerate(subdirs, start=401):
    old_path = os.path.join(parent_dir, subdir)
    new_path = os.path.join(parent_dir, f'Video_{i:04d}')
    os.rename(old_path, new_path)