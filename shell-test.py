import os
import sys
import hashlib

def md5sum(filename):
	with open(filename, 'rb') as file_object:
		file_content = file_object.read()
	file_md5 = hashlib.md5(file_content)
	return file_md5

former_md5 = md5sum("test.txt")
# os.system(command)
while True:
	if former_md5 != md5sum("test.txt"):
		os.system("git add test.txt")
		os.system("git commit -m \"Data changed.\"")
		os.system("git push")
		former_md5 = md5sum("test.txt")
