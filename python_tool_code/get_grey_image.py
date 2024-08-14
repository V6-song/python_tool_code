import cv2
import os

def split_video_into_frames(video_folder_path):
    # 获取文件夹中的所有文件
    files = os.listdir(video_folder_path)

    for file in files:
        # 检查文件是否是视频文件
        if file.endswith(('.mp4', '.avi')):
            # 打开视频文件
            video = cv2.VideoCapture(os.path.join(video_folder_path, file))
            
            # 创建同名文件夹来保存视频帧
            frames_folder_path = os.path.join(video_folder_path, os.path.splitext(file)[0])
            os.makedirs(frames_folder_path, exist_ok=True)
            
            frame_count = 0
            while True:
                # 读取视频的每一帧
                ret, frame = video.read()
                if not ret:
                    break
                
                # 将每一帧保存到新创建的文件夹中
                frame_file_path = os.path.join(frames_folder_path, f'frame_{frame_count}.jpg')
                cv2.imwrite(frame_file_path, frame)
                
                frame_count += 1

# 使用你的视频文件夹路径替换 'your_video_folder_path'
split_video_into_frames('C:/Users/song_/Desktop/PUIE-Net-main/dataset/UVEB_short/short_video_gt')