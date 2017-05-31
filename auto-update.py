import os
import hashlib
from file_reader import read_chunks


def hash_sum(file_name, algorithm="md5"):
    # select algorithm optionally; default is md5
    if algorithm == "md5":
        method = hashlib.md5()
    elif algorithm == "sha1":
        method = hashlib.sha1()

    if isinstance(file_name, basestring) and os.path.exists(file_name):
        with open(file_name, 'rb') as file_object:
            for chunk in read_chunks(file_object):
                method.update(chunk)
    elif file_name.__class__.name__ in ["StringIO", "cStringIO"] or isinstance(file_name, file):
        for chunk in read_chunks(file_name):
            method.update(chunk)
    else:
        return ""
    return method.hexdigest()

if __name__ == '__main__':
    update_times = 0
    filename = raw_input("\nInput the name of file (e.g. test.txt) to be updated automatically:\n")
    former_hash = hash_sum(filename)
    print("************************************************************************")
    print("Session begin.\n")
    print("Press Ctrl + C to terminate if needed.\n")

    try:
        while True:
            if former_hash != hash_sum(filename):
                print("====== Updating data ======")
                os.system("git add {}".format(filename))
                os.system("git commit -m \"Data changed.\"")
                os.system("git push origin master")
                former_hash = hash_sum(filename)
                update_times += 1
                print("====== Data updated ====== for {} times in this session\n"
                      .format(update_times))
                print("Press Ctrl + C to terminate if needed.\n")
    except KeyboardInterrupt:
        print("User interrupt; session terminated.")
        print("************************************************************************")
    except:
        print("Other exceptions occur.")
