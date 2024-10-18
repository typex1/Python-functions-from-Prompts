"""
In the directory tree given by the folder (CLI param), find all duplicate files.
"""
from duplicates_utils import find_duplicate_files as dup
import sys

if len(sys.argv) == 2:
        path_name = sys.argv[1]
else:
        print ("usage: "+sys.argv[0]+" path_name")
        exit(1)

result = dup(path_name)
print("result: {}".format(result))
