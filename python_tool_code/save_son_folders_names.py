"""

我会给出你一个文件夹的绝对路径
该文件夹下面有若干子文件夹
把这些子文件夹的名字写入一个名为list的txt文件中
每一行保存一个子文件夹的名字
把最后的txt文件保存到父文件夹下面

"""

import os

# 给出父文件夹的绝对路径
directory_path = "E:/video1"

# 获取文件夹中的所有条目
entries = os.listdir(directory_path)

# 过滤出所有的子文件夹
subdirectories = [entry for entry in entries if os.path.isdir(os.path.join(directory_path, entry))]

# 将子文件夹的名字写入到list.txt文件中
with open(os.path.join('C:/Users/song_/Desktop','video1.txt'), 'w') as f:
    for subdir in subdirectories:
        f.write(subdir + '\n') #每一行保存一个子文件夹的名字,换行
