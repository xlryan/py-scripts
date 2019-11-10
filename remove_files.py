import os

path = "/Users/ryan/Downloads/"

for root,dirs,files in os.walk(path):
	for file in files:
		if os.path.splitext(file)[1] == ".jpg":
			os.remove(os.path.join(root,file))