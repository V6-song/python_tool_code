"""
    $parent_folder$   
        ├── Folder1    
        │   └── xxx ---→ images 
        ├── Folder2   
        │   └──xxx  ---→ images 
        ...  
        └── Folder_NN    
            └── xxx ---→ images

"""

import cv2
import os

# 父文件夹路径
parent_folder = 'D:/d-f_animals/' 

# 获取所有子文件夹
subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]

# 对每个子文件夹进行迭代
for subfolder in subfolders:
    # 获取子文件夹中的images子文件夹路径
    images_folder = os.path.join(subfolder, 'images')

    # 获取images子文件夹中的所有图像文件
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.jpg') or f.endswith('.png')]

    # 对每个图像文件进行迭代
    for i, image_file in enumerate(image_files):
        # 读取图像
        img_path = os.path.join(images_folder, image_file)
        img = cv2.imread(img_path)

        # 在第一次迭代时创建视频写入器
        if i == 0:
            height, width, _ = img.shape
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用mp4编码
            video_name = os.path.basename(subfolder) + '.mp4'  # 使用子文件夹的名字作为视频的名字
            video_writer = cv2.VideoWriter(os.path.join('D:/d-f_animals/', video_name), fourcc, 10.0, (width, height))  # 使用图像的实际大小

        # 将帧添加到视频中
        video_writer.write(img)

    print(os.path.basename(subfolder), 'Done!')
    # 释放视频写入器
    if 'video_writer' in locals():
        video_writer.release()