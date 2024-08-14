"""
我会给出一个父文件夹的地址
这个父文件夹下存在一系列的子文件夹
请重命名这些子文件夹的名称
在原来名字的基础上在每个子文件夹名字前面加一个数字”18“
"""

# import os

# def rename_subfolders_add_prefix(parent_folder):
#     # 获取父文件夹下的所有子文件夹
#     subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]
#     # 遍历每个子文件夹
#     for subdir in subfolders:
#         # 获取子文件夹的名称
#         subdir_name = os.path.basename(subdir)
#         # 构建新的子文件夹名称，前面加上"18"
#         new_subdir_name = "s" + subdir_name
#         # 构建新的子文件夹路径
#         new_subdir_path = os.path.join(parent_folder, new_subdir_name)
#         # 重命名子文件夹
#         os.rename(subdir, new_subdir_path)
#         print(f"Renamed {subdir} to {new_subdir_path}")

# # 使用示例
# # replace 'your_parent_folder_path' with the actual path of your parent folder
# rename_subfolders_add_prefix('E:/video8')


"""
恢复原名称
"""
# import os

# def restore_subfolders_name(parent_folder):
#     # 获取父文件夹下的所有子文件夹
#     subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]
#     # 遍历每个子文件夹
#     for subdir in subfolders:
#         # 获取子文件夹的名称
#         subdir_name = os.path.basename(subdir)
#         # 检查子文件夹名称是否以"18"开头
#         if subdir_name.startswith("8"):
#             # 移除名称开头的"18"
#             original_subdir_name = subdir_name[2:]
#             # 构建原始子文件夹路径
#             original_subdir_path = os.path.join(parent_folder, original_subdir_name)
#             # 重命名子文件夹，恢复原名称
#             os.rename(subdir, original_subdir_path)
#             print(f"Restored {subdir} to {original_subdir_path}")

# # 使用示例
# restore_subfolders_name('E:/video8')