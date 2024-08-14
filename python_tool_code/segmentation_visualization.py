# import cv2
# import json
# import numpy as np
# import os
# from pycocotools.mask import decode

# # 父文件夹路径
# parent_folder = 'D:/ChengyangSong_0805_frames'

# # 获取所有子文件夹
# subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]

# # 对每个子文件夹进行迭代
# for subfolder in subfolders:
#     # 检查是否存在annotations.json文件
#     if not os.path.exists(os.path.join(subfolder, 'annotations.json')):
#         continue

#     # 读取json文件
#     with open(os.path.join(subfolder, 'annotations.json')) as f:
#         data = json.load(f)

#     # 对每个注释进行迭代
#     for i, annotation in enumerate(data['annotations']):
#         # 获取图像信息
#         image_info = next((item for item in data['images'] if item["id"] == annotation['image_id']), None)
#         if image_info is None:
#             continue

#         # 读取图像
#         img_path = os.path.join(subfolder, image_info['file_name'])
#         img = cv2.imread(img_path)

#         # 在第一次迭代时创建视频写入器
#         if i == 0:
#             height, width, _ = img.shape
#             fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用mp4编码
#             video_name = os.path.basename(subfolder) + '.mp4'  # 使用子文件夹的名字作为视频的名字
#             video_writer = cv2.VideoWriter(os.path.join(subfolder, video_name), fourcc, 30.0, (width, height))  # 使用图像的实际大小

#         # 获取分割信息
#         segm = annotation['segmentation']

#         # 添加分割
#         mask = decode(segm)
#         mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # 将灰度图像转换为BGR图像
#         img = cv2.addWeighted(img, 0.5, mask*255, 0.5, 0)  # 将分割添加到图像上

#         # 将帧添加到视频中
#         video_writer.write(img)

#     print(os.path.basename(subfolder), 'Done!')
#     # 释放视频写入器
#     video_writer.release()



import cv2
import json
import numpy as np
import os
from pycocotools.mask import decode

# 父文件夹路径
parent_folder = 'D:/ChengyangSong_0805_frames'

# 获取所有子文件夹
subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]

# 对每个子文件夹进行迭代
for subfolder in subfolders:
    # 检查是否存在annotations.json文件
    if not os.path.exists(os.path.join(subfolder, 'annotations.json')):
        continue

    # 读取json文件
    with open(os.path.join(subfolder, 'annotations.json')) as f:
        data = json.load(f)

    video_writer = None  # 初始化video_writer

    # 对每个注释进行迭代
    for i, annotation in enumerate(data['annotations']):
        # 获取图像信息
        image_info = next((item for item in data['images'] if item["id"] == annotation['image_id']), None)
        if image_info is None:
            continue

        # 读取图像
        img_path = os.path.join(subfolder, image_info['file_name'])
        img = cv2.imread(img_path)

        # 在第一次迭代时创建视频写入器
        if i == 0:
            height, width, _ = img.shape
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用mp4编码
            video_name = os.path.basename(subfolder) + '.mp4'  # 使用子文件夹的名字作为视频的名字
            video_writer = cv2.VideoWriter(os.path.join(subfolder, video_name), fourcc, 30.0, (width, height))  # 使用图像的实际大小

        # 获取分割信息
        segm = annotation['segmentation']

        # 添加分割
        mask = decode(segm)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # 将灰度图像转换为BGR图像
        img = cv2.addWeighted(img, 0.5, mask*255, 0.5, 0)  # 将分割添加到图像上

        # 将帧添加到视频中
        video_writer.write(img)

    print(os.path.basename(subfolder), 'Done!')
    # 释放视频写入器
    if video_writer is not None:  # 检查video_writer是否为None
        video_writer.release()