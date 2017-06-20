from distutils.dir_util import copy_tree
from sys import argv

destinationFolder = argv[1]

copy_tree('./template', destinationFolder)
