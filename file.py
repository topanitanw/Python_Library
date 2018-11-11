import os 

def abspath(relative_path, filename):
    '''
    Return a absolute path of a file in String.
    '''
    # os.sep = directory separator 
    relative_filepath = relative_path + os.sep + filename
    return os.path.abspath(relative_path)

def listfile(dirpath):
    '''
    Return a list of files in a directory in dirpath.
    '''
    file_lst = []
    path = "."
    for elem in os.listdir(dirpath):
        if os.path.isfile(os.path.join(dirpath, elem)):
            file_lst.append(elem)
    return file_lst
