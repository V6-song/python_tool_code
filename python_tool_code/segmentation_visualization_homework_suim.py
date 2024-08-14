from PIL import Image

def convert_white_to_yellow(image_path):
    # 打开图像，并确保以 RGB 模式打开
    img = Image.open(image_path).convert("RGB")
    # 获取图像的宽度和高度
    width, height = img.size

    # 遍历每个像素
    for y in range(height):
        for x in range(width):
            # 获取当前像素的颜色
            pixel_color = img.getpixel((x, y))
            # 如果像素为白色（255，255，255）
            # if pixel_color == (255, 255, 255):
            if pixel_color == (255, 255, 0):
                # 将白色像素更改为明亮的黄色（255，255，0）
                img.putpixel((x, y), (0, 0,0))  # 顺序为RGB fv 110 ri 101  白色111 黑色000

    # 保存修改后的图像
    img.save("final1.bmp")

# 调用函数并传入图像路径
convert_white_to_yellow("final.bmp")




# from PIL import Image

# def convert_white_to_color(image_path, color):
#     # 打开图像，并确保以 RGB 模式打开
#     img = Image.open(image_path).convert("RGB")
#     # 获取图像的宽度和高度
#     width, height = img.size

#     # 遍历每个像素
#     for y in range(height):
#         for x in range(width):
#             # 获取当前像素的颜色
#             pixel_color = img.getpixel((x, y))
#             # 如果像素为白色（255，255，255）
#             if pixel_color == (255, 255, 255):
#                 # 将白色像素更改为指定颜色
#                 img.putpixel((x, y), color)

#     # 保存修改后的图像
#     img.save("colored_image.bmp")

# # 调用函数并传入图像路径和目标颜色
# convert_white_to_color("C:/Users/song_/Desktop/nl100/fv.bmp", (0, 0, 255))  # 将白色更改为蓝色


