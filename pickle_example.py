'''
Pickle Demonstration

Panitan W
'''

import pickle 

def dump(data, filename):
    '''
    Dump the obj to a file
    '''
    filepickle = open(filename, "wb")
    pickle.dump(data, filepickle)
    filepickle.close()

def load(filename):
    '''
    Load a file and returns an object. This file must be written by using the pickle module
    '''
    filepic = open(filename, "rb")
    obj = pickle.load(filepic)
    filepic.close()
    return obj
