import os
from PIL import Image

# 指定的目录路径
dir_path = "C:/Users/song_/Desktop/SpiralGAN/data/song_test_data/Video_001/imgs"

# 创建一个文本文件来存储图像大小
with open("C:/Users/song_/Desktop/SpiralGAN/data/song_test_data/Video_001/image_sizes.txt", "w") as f:
    # 遍历目录中的所有文件
    for filename in os.listdir(dir_path):
        # 如果这是一个图像文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            try:
                # 获取图像的大小
                image = Image.open(os.path.join(dir_path, filename))
                width, height = image.size
                
                # 将图像大小写入文本文件
                f.write(f"{filename}: {width}x{height}\n")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")