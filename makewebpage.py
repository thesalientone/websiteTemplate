from distutils.dir_util import copy_tree
from os import getcwd
from sys import argv

destinationFolder = argv[1]
pathName = getcwd()
pathName += '/template'
copy_tree(pathName, destinationFolder)
