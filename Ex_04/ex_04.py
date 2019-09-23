#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
from shutil import copyfile

SVN_NAME_FOLDER = ".svn"

if len(sys.argv) > 1:
	num_folder = 0
	for path_obj in Path(sys.argv[1]).glob('**/*'):
		if os.path.isdir(str(path_obj)):
			x_names = str(path_obj).split(os.sep)
			if x_names[len(x_names)-1] == SVN_NAME_FOLDER:
				os.rmdir(str(path_obj))
				num_folder += 1
	print("Numbers of deleted folders : ", num_folder)
else:
	print("Too fiew arguments.")
	print("Use: python ex_04.py <full path folder for scaning svn-folder>")
	print("Example: python ex_05.py /media/paul/Project/CPP/")
