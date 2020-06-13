import os
import sys
import pathlib
from os import listdir
from os.path import isfile, join

path = pathlib.Path().absolute()
if len(sys.argv) == 2:
    path = sys.argv[1]


files = [f for f in listdir(path) if isfile(join(path, f))]
for f in files:
    print(f)

def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

listd = listdirs(path)
for dir in listd:
    print(dir)