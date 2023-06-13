import os

source_dir = r"C:\Users\18089\Downloads"

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)