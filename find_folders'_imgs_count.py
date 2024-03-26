import os

# 指定的目录路径
dir_path = "C:/Users/song_/Desktop/for_enhancement/"

# 图像文件的扩展名
image_extensions = ['.png', '.jpg', '.jpeg', '.bmp']

# 初始化图像文件的数量
total_image_count = 0

# 遍历目录及其所有子目录
for subdir, _, filenames in os.walk(dir_path):
    # 初始化子目录的图像数量
    subdir_image_count = 0

    # 遍历目录中的所有文件
    for filename in filenames:
        # 如果文件是图像文件，增加图像文件的数量
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            subdir_image_count += 1

    # 输出子目录的名称和图像数量
    print(f"Directory: {subdir}, Image count: {subdir_image_count}")

    # 更新总图像数量
    total_image_count += subdir_image_count

# 输出总图像数量
print(f"Total number of image files: {total_image_count}")