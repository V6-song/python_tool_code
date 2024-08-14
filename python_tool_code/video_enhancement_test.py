# import cv2
# import numpy as np
# import os

# cap = cv2.VideoCapture('C://Users//song_//Desktop//python_tool_code//test.mp4')
# frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# print('Frame count:', frame_count)
# # Create a color list
# colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# # Create a directory for frames
# if not os.path.exists('frames'):
#     os.makedirs('frames')

# # Take first frame and find corners in it
# ret, old_frame = cap.read()
# old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
# feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7)
# p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# # Create a mask image for drawing purposes
# mask = np.zeros_like(old_frame)

# frame_index = 0
# while(1):
#     lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Save the frame to a file
#     cv2.imwrite('frames/frame_{:04d}.png'.format(frame_index), frame)
#     frame_index += 1

#     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # calculate optical flow
#     p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

#     if p1 is None:
#         print("Optical flow failed.")
#         break

#     # Select good points
#     good_new = p1[st==1]
#     good_old = p0[st==1]

#     # draw the tracks
#     for i,(new,old) in enumerate(zip(good_new,good_old)):
#         a,b = new.ravel()
#         c,d = old.ravel()
#         mask = cv2.line(mask, (int(a),int(b)),(int(c),int(d)), colors[i % len(colors)], 2)
#         frame = cv2.circle(frame,(int(a),int(b)),5,colors[i % len(colors)],-1)
#     img = cv2.add(frame,mask)

#     cv2.imshow('frame',img)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break

#     # Now update the previous frame and previous points
#     old_gray = frame_gray.copy()
#     p0 = good_new.reshape(-1,1,2)

# cv2.destroyAllWindows()
# cap.release()

# import cv2
# import os

# # 视频的绝对地址
# video_path = 'C://Users//song_//Desktop//python_tool_code//test.mp4'

# # 创建一个新的文件夹来保存帧
# if not os.path.exists('frames'):
#     os.makedirs('frames')

# cap = cv2.VideoCapture(video_path)
# frame_index = 0

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # 保存帧到文件
#     cv2.imwrite('frames/frame_{:04d}.png'.format(frame_index), frame)
#     frame_index += 1

# cap.release()

import cv2
import os

# 视频的绝对地址
video_path = 'C:/Users/song_/Desktop/challenging_videos'

# 创建一个新的文件夹来保存帧
if not os.path.exists('frames'):
    os.makedirs('frames')

# 创建一个新的文件夹来保存帧间隔时间
if not os.path.exists('frames_time'):
    os.makedirs('frames_time')

cap = cv2.VideoCapture(video_path)
frame_index = 0

# 获取视频的帧率
fps = cap.get(cv2.CAP_PROP_FPS)
# 计算每两帧之间的时间间隔
frame_interval = 1.0 / fps

# 创建一个txt文件来保存每两帧之间的时间间隔
with open('frames_time/frame_intervals.txt', 'w') as f:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 保存帧到文件
        cv2.imwrite('frames/frame_{:04d}.png'.format(frame_index), frame)
        # 将每两帧之间的时间间隔写入txt文件
        f.write(str(frame_interval) + '/n')

        frame_index += 1

cap.release()