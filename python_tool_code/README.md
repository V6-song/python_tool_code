# record_folders'_name.py

这个脚本可以记录父文件夹下的子文件夹的名称到**titles.txt**文本文档中，该文档的每一行记录一个子文件夹的名称。值得注意的是，最后的文本文件被保存到父文件夹下。需要给出父文件夹的绝对路径。

# segmentation_visualization.py

父文件夹d-f\_animals，他的下面有多个子文件夹，每个子文件夹下都有embeddings，model，images以及标注的annotation.json文件，script能够自动的处理每个子文件夹，并把可视化的视频的名字命名为与子文件夹名字一样，保存到对应的子文件夹下。FPS=30

# recover_video_from_frames_fps_10.py

获取原视频，文件夹的格式在脚本中给出了，FPS=10,视频存储在了parent_folder下面，视频以子文件夹的名称命名。

# move_images_to_images_folder.py

给出父文件夹绝对路径，父文件夹下存在一系列的子文件夹，子文件夹下一系列图片，在每个子文件夹下创建一个名为images的文件夹，将所有的图片移动到该文件夹下。

# count_images_number.py

父文件夹下面有一系列的子文件夹，每个子文件夹下有个名为images的文件夹，统计每个images下面的图片数量和最后的总的图片数量并打印。需要修改父文件夹的绝对地址。结果打印在终端。

# create_subfolders_according_to_txt_file.py

给出父文件夹的绝对路径，以及一个txt文件，这个txt文件中每一行记录了一个子文件夹的名称，请给据txt文件夹中提供的子文件夹的名称创建这些子文件夹

# move_json_to_same_name_subfolders.py

代码会将源父文件夹下的每个子文件夹中的'annotations.json'文件移动到目标父文件夹下同名的子文件夹中。如果目标父文件夹下没有对应的同名子文件夹，代码会自动创建一个。
