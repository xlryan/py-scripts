import os
import shutil

path = "/Users/ryan/Downloads/"
newpath = "/Users/ryan/Downloads/mp4"

for root,dirs,files in os.walk(path):
	for file in files:
		if os.path.splitext(file)[1] == ".mp4":
			shutil.move(os.path.join(root,file),os.path.join(newpath,file))