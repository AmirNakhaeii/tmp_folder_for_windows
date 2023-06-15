
import os
import shutil

base_path = f"C:{os.getenv('HOMEPATH')}\Desktop\\"
dir_name = 'tmp'
dir_path = base_path + dir_name

try:
    shutil.rmtree(dir_path)
    os.mkdir(dir_path)
except FileNotFoundError:
    ...
