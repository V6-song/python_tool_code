import os

def count_images(parent_folder):
    total_images = 0
    for dirpath, dirnames, filenames in os.walk(parent_folder):
        if os.path.basename(dirpath) == 'images':
            image_count = 0
            for filename in filenames:
                if os.path.splitext(filename)[1] in ['.jpg', '.jpeg', '.png', '.bmp']:
                    image_count += 1
            print(f'Images in {dirpath}: {image_count}')
            total_images += image_count
    print(f'Total images: {total_images}')

# 使用方法
# count_images('D:/New_data_frames')
count_images('E:/zzq123/zzq3')