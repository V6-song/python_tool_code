import os

def record_subfolder_names(parent_folder):
    # 创建一个名为"titles.txt"的文件
    with open(os.path.join('C:/Users/song_/Desktop', 'g-n_animals titles.txt'), 'w') as f:
        # 遍历父文件夹下的所有子文件夹
        for subdir in os.listdir(parent_folder):
            subdir_path = os.path.join(parent_folder, subdir)
            # 确保这是一个文件夹，而不是一个文件
            if os.path.isdir(subdir_path):
                # 将子文件夹的名字写入文件
                f.write(subdir + '\n')

# 使用你的父文件夹路径替换下面的路径
record_subfolder_names('F:/ChengyangSong_0805_frames')