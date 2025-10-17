import kagglehub
import shutil
import os

"""_summary_
这个脚本用于从 Kaggle Hub 下载一个数据集，并将其复制到指定的目标目录中。
这个数据集暂存在downloaded_data文件夹中，然后通过data_divide.py进行二次处理，最后正确放在data文件夹中。
"""


# Download latest version
path = kagglehub.dataset_download("liaolianfoka/met-meme")

print("Path to dataset files:", path)

if not os.path.exists("downloaded_data"):
    os.makedirs("downloaded_data")
target_dir = "./downloaded_data"
# 复制到目标位置（或使用 shutil.move 如果不需要保留缓存）
shutil.copytree(path, target_dir, dirs_exist_ok=True)

print("Dataset copied to:", target_dir)
