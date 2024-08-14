"""
    给出一个父文件夹的路径
    父文件夹下存在一系列的子文件夹
    每个子文件夹下面都有一个json格式的文件
    把这些json文件重新命名为与子文件夹相同的名称
    然后将每个子文件夹下面的json文件复制到父文件夹下面
"""

import os
import shutil

def rename_and_copy_json(parent_folder):
    # 遍历父文件夹中的每个子文件夹
    for subdir, dirs, files in os.walk(parent_folder):
        for filename in files:
            if filename.endswith('.json'):
                # 构建原始json文件的完整路径
                original_path = os.path.join(subdir, filename)
                # 获取子文件夹的名称
                subdir_name = os.path.basename(subdir)
                # 构建新的文件名和路径
                new_filename = f"{subdir_name}.json"
                new_path = os.path.join(parent_folder, new_filename)
                # 复制并重命名json文件到父文件夹
                shutil.copy2(original_path, new_path)
                print(f"Copied and renamed {filename} to {new_path}")

# 使用示例
# replace 'your_parent_folder_path' with the actual path of your parent folder
rename_and_copy_json('E:/zzq123/zzq3')