import os
import sys
import hashlib


def md5sum(filename):
    with open(filename, 'rb') as file_object:
        file_object.seek(0)
        file_content = file_object.read()
    file_md5 = hashlib.md5(file_content)
    return file_md5

print("Session begin.")
update_times = 0
former_md5 = md5sum("test.txt")

while True:
    if former_md5 != md5sum("test.txt"):
        print("====== Updating data ======")
        os.system("git add test.txt")
        os.system("git commit -m \"Data changed.\"")
        # os.system("git push origin master")
        former_md5 = md5sum("test.txt")
        update_times += 1
        print("====== Data updated for {} times in this session. ======".format(update_times))
