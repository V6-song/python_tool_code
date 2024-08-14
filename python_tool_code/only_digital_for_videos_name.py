# import os
# import re

# def rename_files_in_folder(folder_path):
#     for filename in os.listdir(folder_path):
#         new_name = ''.join(re.findall(r'/d+', filename))
#         if new_name:
#             new_name += os.path.splitext(filename)[1]  # keep the file extension
#             os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

# # 使用方法
# # rename_files_in_folder('your_folder_path')
# # 使用方法
# rename_files_in_folder('../UVEB/train/label/O')


import os
import cv2

def split_videos_into_frames(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.mp4', '.avi', '.mov')):  # check if the file is a video file
            video_path = os.path.join(folder_path, filename)
            video = cv2.VideoCapture(video_path)
            fps = video.get(cv2.CAP_PROP_FPS)
            frame_count = 0
            while True:
                ret, frame = video.read()
                if ret:
                    base_filename = os.path.splitext(filename)[0]  # get the filename without extension
                    cv2.imwrite(os.path.join(folder_path, f'{frame_count}_{base_filename}.jpg'), frame)
                    frame_count += 1
                else:
                    break
            video.release()
            os.remove(video_path)  # delete the original video file

# 使用方法
split_videos_into_frames('../PUIE-Net-main/dataset/UVEB_part/test/image')