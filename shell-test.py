import os
# import sys
import hashlib

def md5sum(filename):
    with open(filename, 'rb') as file_object:
        file_content = file_object.read()
    m = hashlib.md5(file_content)
    file_md5 = m.hexdigest()
    return file_md5

print("Session begin.")
update_times = 0
former_md5 = md5sum("test.txt")

while True:
    if former_md5 != md5sum("test.txt"):
        print("====== Updating data ======")
        os.system("git add test.txt")
        os.system("git commit -m \"Data changed.\"")
        os.system("git push origin master")
        former_md5 = md5sum("test.txt")
        update_times += 1
        print("====== Data updated ====== for {} times in this session\n".format(update_times))

'''

see: http://sjq597.github.io/2015/12/18/Python-MD5%E6%A3%80%E9%AA%8C%E6%96%87%E4%BB%B6/

def read_chunks(fp):
    fp.seek(0)
    chunk = fp.read(8 * 1024)
    while chunk:
        yield chunk
        chunk = fp.read(8 * 1024)
    else: 
        fp.seek(0)

'''
