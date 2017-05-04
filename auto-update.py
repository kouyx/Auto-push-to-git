import os
import hashlib


def hashsum(file_name, algorithm="md5"):
    # read 8K of file content (as a chunk) at one time
    def read_chunks(file_object):
        file_object.seek(0)
        chunk = file_object.read(8 * 1024)
        while chunk:
            yield chunk
            chunk = file_object.read(8 * 1024)
        else:
            file_object.seek(0)

    # select algorithm optionally; default is md5
    if algorithm == "md5":
        method = hashlib.md5()
    elif algorithm == "sha1":
        method = hashlib.sha1()
    # read file
    if isinstance(file_name, basestring) and os.path.exists(file_name):
        with open(file_name, 'rb') as file_object:
            for chunk in read_chunks(file_object):
                method.update(chunk)
    elif file_name.__class__.name__ in ["StringIO", "cStringIO"] \
            or isinstance(file_name, file):
        for chunk in read_chunks(file_name):
            method.update(chunk)
    else:
        return ""
    return method.hexdigest()


update_times = 0
filename = raw_input("\nInput the name of file (e.g. test.txt)"
                     " to be updated automatically:\n")
former_hash = hashsum(filename)
print("************************************************************************")
print("Session begin.\n")
print("Press Ctrl + C to terminate if needed.\n")

try:
    while True:
        if former_hash != hashsum(filename):
            print("====== Updating data ======")
            os.system("git add {}".format(filename))
            os.system("git commit -m \"Data changed.\"")
            # os.system("git push origin master")
            former_hash = hashsum(filename)
            update_times += 1
            print("====== Data updated ====== for {} times in this session\n"
                  .format(update_times))
            print("Press Ctrl + C to terminate if needed.\n")
except KeyboardInterrupt:
    print("User interrupt; session terminated.")
    print("************************************************************************")
except:
    print("Other exceptions occur.")
