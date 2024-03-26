# import os
# from PIL import Image

# # 指定的目录路径
# dir_path = "C:/Users/song_/Desktop/SpiralGAN/data/song_test_data/Video_002/imgs"

# # 目标尺寸
# target_width, target_height = 1280, 704

# # 获取目录中的所有图像文件
# image_files = [f for f in os.listdir(dir_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
# total_files = len(image_files)

# # 遍历目录中的所有文件
# for i, filename in enumerate(image_files, start=1):
#     try:
#         # 打开图像
#         image = Image.open(os.path.join(dir_path, filename))
#         width, height = image.size

#         # 如果宽度大于目标宽度，调整宽度
#         if width > target_width:
#             width = target_width

#         # 如果高度大于目标高度，调整高度
#         if height > target_height:
#             height = target_height

#         # 调整图像大小
#         image = image.resize((width, height))

#         # 保存图像
#         image.save(os.path.join(dir_path, filename))

#         # 输出进度
#         print(f"Processed {i} of {total_files} files ({i/total_files*100:.2f}%)")
#     except Exception as e:
#         print(f"Error processing file {filename}: {e}")




# import os
# from PIL import Image

# # 指定的目录路径
# # root_dir_path = "C:/Users/song_/Desktop/SpiralGAN/song_uvot_test_data"
# root_dir_path = "C:/Users/song_/Desktop/0027"

# # 目标尺寸
# target_width, target_height = 1920, 1056

# # 遍历根目录及其所有子目录
# for dir_path, _, filenames in os.walk(root_dir_path):
#     # 获取目录中的所有图像文件
#     image_files = [f for f in filenames if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
#     total_files = len(image_files)

#     # 遍历目录中的所有文件
#     for i, filename in enumerate(image_files, start=1):
#         try:
#             # 打开图像
#             image = Image.open(os.path.join(dir_path, filename))
#             width, height = image.size

#             # 如果图像的尺寸已经符合要求，跳过当前的循环迭代
#             if width <= target_width and height <= target_height:
#                 continue

#             # 如果宽度大于目标宽度，调整宽度
#             if width > target_width:
#                 width = target_width

#             # 如果高度大于目标高度，调整高度
#             if height > target_height:
#                 height = target_height

#             # 调整图像大小
#             image = image.resize((width, height))

#             # 保存图像
#             image.save(os.path.join(dir_path, filename))

#             # 输出进度
#             print(f"Processed {i} of {total_files} files in {dir_path} ({i/total_files*100:.2f}%)")
#         except Exception as e:
#             print(f"Error processing file {filename} in {dir_path}: {e}")


    # 先判断图片大小,一共有四种规格的图片:840×2160，640×360，540×960，1920×1080。
    # 如果图片大小为3840×2160，那么将图片裁剪为3840×2144，如果图片大小为640×360，那么将图片修改为640×352，
    # 如果图片大小为540×960，将图片大小改为512×960，如果图片大小为1920×1080，将图片大小修改为1920×1056.
    # 给出我修改后的代码。

import os
from PIL import Image

# 指定的目录路径
root_dir_path = "C:/Users/song_/Desktop/for_enhancement"

# 原始尺寸到目标尺寸的映射
size_mapping = {
    (3840, 2160): (3840, 2144),
    (640, 360): (640, 352),
    (540, 960): (512, 960),
    (1920, 1080): (1920, 1056)
}

# 遍历根目录及其所有子目录
for dir_path, _, filenames in os.walk(root_dir_path):
    # 获取目录中的所有图像文件
    image_files = [f for f in filenames if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    total_files = len(image_files)

    # 遍历目录中的所有文件
    for i, filename in enumerate(image_files, start=1):
        try:
            # 打开图像
            image = Image.open(os.path.join(dir_path, filename))
            width, height = image.size

            # 如果图像的尺寸在映射中
            if (width, height) in size_mapping:
                # 获取目标尺寸
                target_width, target_height = size_mapping[(width, height)]

                # 调整图像大小
                image = image.resize((target_width, target_height))

                # 保存图像
                image.save(os.path.join(dir_path, filename))

                # 输出进度
                print(f"Processed {i} of {total_files} files in {dir_path} ({i/total_files*100:.2f}%)")
        except Exception as e:
            print(f"Error processing file {filename} in {dir_path}: {e}")



# 对上面的操作执行反向操作，先检测现在图片的大小，恢复到原来图片的大小，需要填补的地方用黑色进行填补

# import os
# from PIL import Image, ImageOps

# # 指定的目录路径
# root_dir_path = "C:/Users/song_/Desktop/0027"

# # 目标尺寸到原始尺寸的映射
# size_mapping = {
#     (3840, 2144): (3840, 2160),
#     (640, 352): (640, 360),
#     (512, 960): (540, 960),
#     (1920, 1056): (1920, 1080)
# }

# # 遍历根目录及其所有子目录
# for dir_path, _, filenames in os.walk(root_dir_path):
#     # 获取目录中的所有图像文件
#     image_files = [f for f in filenames if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
#     total_files = len(image_files)

#     # 遍历目录中的所有文件
#     for i, filename in enumerate(image_files, start=1):
#         try:
#             # 打开图像
#             image = Image.open(os.path.join(dir_path, filename))
#             width, height = image.size

#             # 如果图像的尺寸在映射中
#             if (width, height) in size_mapping:
#                 # 获取原始尺寸
#                 original_width, original_height = size_mapping[(width, height)]

#                 # 调整图像大小
#                 image = image.resize((width, height), Image.ANTIALIAS)

#                 # 计算需要填充的边缘大小
#                 padding = (0, 0, original_width - width, original_height - height)

#                 # 使用黑色填充图像
#                 image = ImageOps.expand(image, padding, fill='black')

#                 # 保存图像
#                 image.save(os.path.join(dir_path, filename))

#                 # 输出进度
#                 print(f"Processed {i} of {total_files} files in {dir_path} ({i/total_files*100:.2f}%)")
#         except Exception as e:
#             print(f"Error processing file {filename} in {dir_path}: {e}")




# # 这是修改后的代码，我使用ImageOps.expand方法将图像扩展到1920x1080，用黑色填充新增的部分。

# import os
# from PIL import Image, ImageOps

# # 指定的目录路径
# root_dir_path = "C:/Users/song_/Desktop/targets"

# # 目标尺寸
# target_width, target_height = 1920,1080             ###########修改需要的尺寸

# # 遍历根目录及其所有子目录
# for dir_path, _, filenames in os.walk(root_dir_path):
#     # 获取目录中的所有图像文件
#     image_files = [f for f in filenames if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
#     total_files = len(image_files)

#     # 遍历目录中的所有文件
#     for i, filename in enumerate(image_files, start=1):
#         try:
#             # 打开图像
#             image = Image.open(os.path.join(dir_path, filename))
#             width, height = image.size

#             # 如果图像的尺寸已经符合要求，跳过当前的循环迭代
#             if width == target_width and height == target_height:
#                 continue

#             # 调整图像大小
#             image = image.resize((width, height), Image.ANTIALIAS)

#             # 计算需要填充的边缘大小
#             padding = (0, 0, target_width - width, target_height - height)

#             # 使用黑色填充图像
#             image = ImageOps.expand(image, padding, fill='black')

#             # 保存图像
#             image.save(os.path.join(dir_path, filename))

#             # 输出进度
#             print(f"Processed {i} of {total_files} files in {dir_path} ({i/total_files*100:.2f}%)")
#         except Exception as e:
#             print(f"Error processing file {filename} in {dir_path}: {e}")
# #这样，每个处理后的图像都会被扩展到1920x1080，新增的部分将被黑色填充。






# # 有一个文件夹，我会给出你绝对路径，它里面有一系列以Video_命名的文件夹，
# # 每个文件夹下面还有一个子文件与其父文件夹的名字相同，
# # 请把这些子文件夹移动到目标文件夹，我会给出你目标文件夹的绝对地址。给出我代码
            
# import os
# import shutil

# # 源目录和目标目录的绝对路径
# source_dir_path = "C:/Users/song_/Desktop/Videos_Parent_Folder_enhanced"
# target_dir_path = "C:/Users/song_/Desktop/targets"

# # 遍历源目录及其所有子目录
# for dir_path, dirnames, _ in os.walk(source_dir_path):
#     # 获取所有以"Video_"开头的子目录
#     video_dirs = [d for d in dirnames if d.startswith("Video_")]

#     # 遍历所有的"Video_"子目录
#     for video_dir in video_dirs:
#         # 子目录的完整路径
#         full_dir_path = os.path.join(dir_path, video_dir)

#         # 如果子目录下存在与其名字相同的子目录
#         if os.path.exists(os.path.join(full_dir_path, video_dir)):
#             # 将子目录移动到目标目录
#             shutil.move(os.path.join(full_dir_path, video_dir), target_dir_path)