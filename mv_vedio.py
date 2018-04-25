import os
import shutil

dir_name = os.path.dirname(__file__)

src_path = os.path.join(dir_name, 'Django_1')
dst_path = os.path.join(dir_name, "Django")

for dir in os.listdir(src_path):
    os.makedirs(os.path.join(dst_path, dir))
    for d in os.listdir(os.path.join(src_path, dir)):
        if d!='video':
            shutil.copytree(os.path.join(src_path, dir, d), os.path.join(dst_path, dir, d))



