
import os

path = f"C:{os.getenv('HOMEPATH')}\Desktop\\"

dir_name = 'tmp'

try:
    os.mkdir(path + dir_name)
except FileExistsError:
    os.rename(path + dir_name, path + dir_name + "_1")
    os.mkdir(path + dir_name)
