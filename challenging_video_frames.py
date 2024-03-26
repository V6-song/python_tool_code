import cv2
import os

# 给定的视频文件夹的绝对地址
video_folder = 'C:/Users/song_/Desktop/challenging_videos'

# 遍历文件夹，找到所有的视频文件
for filename in os.listdir(video_folder):
    if filename.endswith('.mp4'):  # 假设视频文件的扩展名是.mp4
        video_path = os.path.join(video_folder, filename)
        video_name = os.path.splitext(filename)[0]  # 获取视频的名字，不包括扩展名

        # 创建一个以视频名命名的文件夹
        video_folder_path = os.path.join(video_folder, video_name)
        if not os.path.exists(video_folder_path):
            os.makedirs(video_folder_path)

        # 在该文件夹下创建一个名为imgs的子文件夹
        imgs_folder_path = os.path.join(video_folder_path, 'imgs')
        if not os.path.exists(imgs_folder_path):
            os.makedirs(imgs_folder_path)

        cap = cv2.VideoCapture(video_path)
        frame_index = 1  # 帧的索引，从0001开始

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 保存帧到文件，图片的名字从0001开始，依次递增
            cv2.imwrite(os.path.join(imgs_folder_path, '{:04d}.png'.format(frame_index)), frame)
            frame_index += 1

        cap.release()