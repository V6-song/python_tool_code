#=======================================================================================
#将video文件夹下面与img文件夹命名为video文件夹
#
# import os
#
# def rename_subfolder_imgs(parent_folder):
#     # 遍历parent_folder下的所有子文件夹
#     for folder_name in os.listdir(parent_folder):
#         subfolder_path = os.path.join(parent_folder, folder_name)
#         # 检查是否为文件夹
#         if os.path.isdir(subfolder_path):
#             # 检查是否存在名为imgs的子文件夹
#             imgs_folder_path = os.path.join(subfolder_path, 'imgs')
#             if os.path.exists(imgs_folder_path):
#                 # 重命名imgs文件夹为其父文件夹的名称
#                 new_name = os.path.join(subfolder_path, folder_name)
#                 os.rename(imgs_folder_path, new_name)
#
# # 调用函数，传入Videos_Parent_Folder的绝对地址
# rename_subfolder_imgs('C:/Users/song_/Desktop/Videos_Parent_Folder')
#=======================================================================================

#=======================================================================================
#子文件夹和父文件夹同名时候把子文件夹名字改为imgs
# # Path: restore_subfolder_name.py
# import os

# def restore_subfolder_name(parent_folder):
#     # 遍历parent_folder下的所有子文件夹
#     for folder_name in os.listdir(parent_folder):
#         subfolder_path = os.path.join(parent_folder, folder_name)
#         # 检查是否为文件夹
#         if os.path.isdir(subfolder_path):
#             # 检查是否存在名为父文件夹名字的子文件夹
#             renamed_folder_path = os.path.join(subfolder_path, folder_name)
#             if os.path.exists(renamed_folder_path):
#                 # 重命名文件夹为"imgs"
#                 new_name = os.path.join(subfolder_path, 'imgs')
#                 os.rename(renamed_folder_path, new_name)

# # 调用函数，传入Videos_Parent_Folder的绝对地址
# restore_subfolder_name('C:/Users/song_/Desktop/Videos_Parent_Folder')
#=======================================================================================

#=======================================================================================
#将video文件下面的同名video子文件夹移动到指定的文件夹

#
# import os
# import shutil
#
# def move_renamed_folders(parent_folder, target_folder):
#     # 遍历parent_folder下的所有子文件夹
#     for folder_name in os.listdir(parent_folder):
#         subfolder_path = os.path.join(parent_folder, folder_name)
#         # 检查是否为文件夹
#         if os.path.isdir(subfolder_path):
#             # 检查是否存在名为父文件夹名字的子文件夹
#             renamed_folder_path = os.path.join(subfolder_path, folder_name)
#             if os.path.exists(renamed_folder_path):
#                 # 移动文件夹到目标文件夹
#                 shutil.move(renamed_folder_path, os.path.join(target_folder, folder_name))
#
# # 调用函数，传入Videos_Parent_Folder的绝对地址和目标文件夹的绝对地址
# # move_renamed_folders('C:/Users/song_/Desktop/Videos_Parent_Folder', '你的目标文件夹的绝对地址')
# move_renamed_folders('C:/Users/song_/Desktop/Videos_Parent_Folder', 'C:/Users/song_/Desktop/for_enhancement')
#=======================================================================================

#=======================================================================================

# # Path: reverse_move_and_rename.py
# import os
# import shutil
#
# def reverse_move_and_rename(target_folder, parent_folder):
#     # 遍历target_folder下的所有子文件夹
#     for folder_name in os.listdir(target_folder):
#         moved_folder_path = os.path.join(target_folder, folder_name)
#         # 检查是否为文件夹
#         if os.path.isdir(moved_folder_path):
#             # 移动文件夹回原来的父文件夹
#             original_folder_path = os.path.join(parent_folder, folder_name)
#             shutil.move(moved_folder_path, original_folder_path)
#             # 重命名文件夹为"imgs"
#             new_name = os.path.join(parent_folder, folder_name, 'imgs')
#             os.rename(original_folder_path, new_name)
#
# # 调用函数，传入目标文件夹的绝对地址和Videos_Parent_Folder的绝对地址
# reverse_move_and_rename('C:/Users/song_/Desktop/1st_quality_worse_hanced', 'C:/Users/song_/Desktop/Videos_Parent_Folder')
# #=======================================================================================

#=======================================================================================
# """"
# 我有一个以Videos_Parent_Folder命名的文件夹,下面有一系列以Video_命名的文件夹,
# 在这些文件夹的里面还有一个以Video_命名的子文件夹,请把这些子文件夹的名字都改为imgs,
# 给出我实现的程序,我会给出你Videos_Parent_Folder的绝对地址
# """

import os

def rename_subfolders(parent_folder):
    # 遍历parent_folder下的所有子文件夹
    for folder_name in os.listdir(parent_folder):
        subfolder_path = os.path.join(parent_folder, folder_name)
        # 检查是否为文件夹
        if os.path.isdir(subfolder_path):
            # 遍历子文件夹下的所有文件和文件夹
            for subfolder_name in os.listdir(subfolder_path):
                original_subfolder_path = os.path.join(subfolder_path, subfolder_name)
                # 检查是否为文件夹
                if os.path.isdir(original_subfolder_path):
                    # 将子文件夹的名字改为"imgs"
                    new_name = os.path.join(subfolder_path, 'imgs')
                    os.rename(original_subfolder_path, new_name)

# 调用函数，传入Videos_Parent_Folder的绝对地址
rename_subfolders('C:/Users/song_/Desktop/Videos_Parent_Folder')

#=======================================================================================