import os
import json

# 你的数据集的路径
data_dir = 'C://Users//song_//Desktop//song_train_dataset'
sequence_dirs = os.listdir(data_dir)

annotations = {}
for sequence_dir in sequence_dirs:
    sequence_path = os.path.join(data_dir, sequence_dir)
    img_dir = os.path.join(sequence_path, 'imgs')  # 图像存储在'imgs'文件夹中
    image_names = sorted([img for img in os.listdir(img_dir) if img.endswith('.jpg')])  # 假设帧是jpg格式
    with open(os.path.join(sequence_path, 'groundtruth_rect.txt'), 'r') as f:
        groundtruths = [line.strip() for line in f]
    if len(image_names) != len(groundtruths):
        print(f"Warning: number of images and groundtruths do not match in {sequence_dir}")
        continue
    annotations[sequence_dir] = list(zip(image_names, groundtruths))

# 将字典保存为JSON文件
with open('annotations.json', 'w') as f:
    json.dump(annotations, f)