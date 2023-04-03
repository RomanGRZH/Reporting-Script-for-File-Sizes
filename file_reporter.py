import os
from os.path import abspath, join, getsize

sizes = {}

user_path = input("Enter directory path:")

for top_dir, directories, files in os.walk(user_path):
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        sizes[full_path] = size
        

sorted_results = sorted(sizes, key=sizes.get, reverse=True)

for path in sorted_results[:20]:
    print("Path: {0}, size: {1}".format(path, sizes[path]))

    