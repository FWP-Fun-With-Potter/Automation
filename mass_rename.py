import os
from pathlib import Path

directory = Path(r"path")

os.chdir(directory)

all = os.listdir()

for folder in all:
    if os.path.isdir(os.path.join(directory, folder)):
        os.chdir(os.path.join(directory, folder))
        items = os.listdir()
        for item in items:
            current_name = item.split("-")
            new_name = current_name[1].split(".")[0][1:] + '-' + current_name[0][:-1] + '.' + current_name[-1].split(".")[-1][:]
            os.rename(item, new_name)
    else:
        items = os.listdir()
        for item in items:
            current_name = item.split("-")
            new_name = current_name[1].split(".")[0][1:] + '-' + current_name[0][:-1] + '.' + current_name[-1].split(".")[-1][:]
            os.rename(item, new_name)