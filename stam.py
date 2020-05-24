import os
import sys

(program_name, path, old_suffix, new_suffix) = sys.argv
for name in os.listdir(path):
    if name.endswith(old_suffix):
        filename = path+name
        newname = filename[:-3] + new_suffix
        print("rename: %s => %s"%(filename, newname))
        os.rename(filename,newname)