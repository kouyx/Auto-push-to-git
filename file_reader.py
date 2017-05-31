import os


def read_chunks(file_object, num_Kibit=8):
    """
    Read chunk_size (default is 8Kibit) of file content at one time
    """
    file_object.seek(0)
    chunk_size = num_Kibit * 1024
    chunk = file_object.read(chunk_size)
    while chunk:
        yield chunk
        chunk = file_object.read(chunk_size)
    else:
        file_object.seek(0)


def file_content(file_name):
    content = ""
    if isinstance(file_name, (str, unicode)) and os.path.exists(file_name):
        with open(file_name, 'rU') as file_object:
            for chunk in read_chunks(file_object):
                content += chunk
    elif file_name.__class__.name__ in ["StringIO", "cStringIO"] or isinstance(file_name, file):
        for chunk in read_chunks(file_name):
            content += chunk
    else:
        print("{} not found.".format(file_name))

    return content


def content_slice(content):
    start_here = 0
    end_here = len(content)
    if 'y' == raw_input("--- Need a slice of the file content? ---\n(Y/y for yes; others for no) ").lower():
        start_label = raw_input(
            "------ Paste the 1st sentence to start with (or leave empty to start from the very beginning) ------\n")
        if start_label != "":
            try:
                start_here = content.index(start_label)
            except ValueError:
                print("\"{}\" \n not found. Start from the very beginning.".format(start_label))

        end_label = raw_input("------ Paste the last sentence to end with (or leave empty to end at the last) ------\n")
        if end_label != "":
            try:
                end_here = content.index(end_label) + len(end_label)
            except ValueError:
                print("\"{}\" \n not found. End at the last.".format(end_label))

    return content[start_here:end_here]
