import os, re, fnmatch

image_path = "X:\\01-WIN10-TMP\\Desktop"
pattern = "^.*.(txt|xlsx)$"

for path, subdirs, files in os.walk(image_path):
    for name in files:
        if re.search(pattern, name):
            print(os.path.join(path, name))
