"""
    给出父文件夹的路径
    父文件夹下存在一系列的子文件
    删除每个子文件下面的embeddings和models文件夹
    其他的文件和文件夹保持不变
"""

import os
import shutil

def delete_specific_subfolders(parent_folder):
    # 遍历父文件夹下的所有子文件夹
    for subdir in next(os.walk(parent_folder))[1]:
        subdir_path = os.path.join(parent_folder, subdir)
        # 定义要删除的文件夹名称列表
        folders_to_delete = ['embeddings', 'models']
        # 遍历每个要删除的文件夹名称
        for folder_name in folders_to_delete:
            folder_path = os.path.join(subdir_path, folder_name)
            # 检查文件夹是否存在
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                # 删除文件夹
                shutil.rmtree(folder_path)
                print(f"Deleted {folder_path}")

# 使用示例
# replace 'your_parent_folder_path' with the actual path of your parent folder
delete_specific_subfolders('E:/zzq123/zzq3')