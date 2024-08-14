import os
import shutil

def move_images_to_subfolder(parent_folder):
    # 遍历父文件夹下的所有子文件夹
    for subdir in os.listdir(parent_folder):
        subdir_path = os.path.join(parent_folder, subdir)
        # 确保这是一个文件夹，而不是一个文件
        if os.path.isdir(subdir_path):
            images_folder = os.path.join(subdir_path, 'images')
            # 如果"images"文件夹已经存在，跳过当前子文件夹
            if os.path.exists(images_folder):
                continue
            # 创建名为"images"的新文件夹
            os.makedirs(images_folder, exist_ok=True)
            # 遍历子文件夹下的所有文件
            for filename in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, filename)
                # 确保这是一个文件，而不是一个文件夹
                if os.path.isfile(file_path):
                    # 检查文件扩展名，如果它是一个图片文件，就移动它
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                        shutil.move(file_path, images_folder)

# 使用你的父文件夹路径替换下面的路径
move_images_to_subfolder('D:/ChengyangSong_0805_frames')