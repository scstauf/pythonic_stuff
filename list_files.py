import sys
import pathlib
import os

walkpath = ''
ext_match = ''
my_files = []

class FileInfo(object):
	len = 0
	path = ''

def file_len(fname):
	try:
		with open(fname) as f:
			for i, l in enumerate(f):
				pass
		return i + 1
	except:
		return 0
	
if len(sys.argv) == 1:
	print('specify a directory to walk')
	exit()
else:
	walkpath = sys.argv[1]
	if not os.path.exists(os.path.dirname(walkpath)):
		print('path does not exist: ' + walkpath)
		exit()
	else:
		print('walking ' + sys.argv[1])
	
	if len(sys.argv) == 3:
		ext_match = sys.argv[2]

if len(walkpath) > 0:
	for path, subdirs, files in os.walk(walkpath):
		for name in files:
			pure_path = pathlib.PurePath(path, name)
			ext = pure_path.suffix
			
			if len(ext_match) > 0 and ext_match != ext:
				continue
			elif len(ext_match) == 0:
				print(pure_path)
			else:
				fi = FileInfo()
				fi.path = str(pure_path)
				fi.len = file_len(pure_path)
				my_files.append(fi)

if len(my_files) > 0:
	my_files.sort(key=lambda x: x.len, reverse=True)

	for my_file in my_files:
		print(str(my_file.len) + ':\t' + my_file.path)