
import os

path = f"C:{os.getenv('HOMEPATH')}\Desktop\\"

dir_name = 'tmp'

try:
    os.mkdir(path + dir_name)
except FileExistsError:
    print(f"'{dir_name}' already exists.")