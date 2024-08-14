from PIL import Image

def overlay_images(image1_path, image2_path, output_path):
    # 打开第一张图片
    img1 = Image.open(image1_path).convert("RGBA")
    # 打开第二张图片
    img2 = Image.open(image2_path).convert("RGBA")

    # 确保图片的尺寸相同
    assert img1.size == img2.size, "Images must have the same dimensions."

    # 创建一个新的空白图像，与原始图像大小相同
    merged_img = Image.new("RGBA", img1.size)

    # 混合两张图片的像素值，调整混合比例以提亮颜色
    for y in range(img1.height):
        for x in range(img1.width):
            # 获取每个像素的 RGBA 值
            r1, g1, b1, a1 = img1.getpixel((x, y))
            r2, g2, b2, a2 = img2.getpixel((x, y))
            # 按照一定比例混合像素值
            r = int((r1 + r2) * 1)  # 调整混合比例，使颜色更明亮
            g = int((g1 + g2) * 1)
            b = int((b1 + b2) * 1)
            a = max(a1, a2)
            # 将混合后的像素值设置到新图像上
            merged_img.putpixel((x, y), (r, g, b, a))

    # 保存合成后的图像
    merged_img.save(output_path)

# 调用函数并传入两张图片的路径和输出路径
overlay_images("./1948fv.bmp", "1948ri.bmp", "1948_final.bmp")



# from PIL import Image

# def overlay_images(image1_path, image2_path, output_path):
#     # 打开第一张图片
#     img1 = Image.open(image1_path).convert("RGBA")
#     # 打开第二张图片
#     img2 = Image.open(image2_path).convert("RGBA")

#     # 确保图片的尺寸相同
#     assert img1.size == img2.size, "Images must have the same dimensions."

#     # 创建一个新的空白图像，与原始图像大小相同
#     merged_img = Image.new("RGBA", img1.size)

#     # 混合两张图片的像素值，调整混合比例以提亮颜色
#     for y in range(img1.height):
#         for x in range(img1.width):
#             # 获取每个像素的 RGBA 值
#             r1, g1, b1, a1 = img1.getpixel((x, y))
#             r2, g2, b2, a2 = img2.getpixel((x, y))
#             # 按照一定比例混合像素值
#             r = (r1 + r2) // 2  # 将相加后的值除以 2
#             g = (g1 + g2) // 2
#             b = (b1 + b2) // 2
#             a = max(a1, a2)
#             # 将混合后的像素值设置到新图像上
#             merged_img.putpixel((x, y), (r, g, b, a))

#     # 保存合成后的图像
#     merged_img.save(output_path)

# # 调用函数并传入两张图片的路径和输出路径
# overlay_images("./1948fv.bmp", "1948ri.bmp", "1948_final.bmp")

