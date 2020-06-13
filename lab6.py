import os
import sys
import pathlib
from os import listdir
from os.path import isfile, join

path = pathlib.Path().absolute()
if len(sys.argv) == 2:
    path = sys.argv[1]


files = [f for f in listdir(path) if isfile(join(path, f))]


list_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

files_and_dirs = files + list_dirs

sorted_fd = sorted(files_and_dirs, key=str.lower)

for file in sorted_fd:
    print(file)