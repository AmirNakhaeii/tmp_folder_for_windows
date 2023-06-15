
import os

path = f"C:{os.getenv('HOMEPATH')}\Desktop\\"

dir_name = 'tmp'

try:
    os.rmdir(path + dir_name)
    os.mkdir(path + dir_name)
except FileNotFoundError:
    ...
