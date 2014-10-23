__author__ = 'hyphen'
import os
import pdb
def search(s):
    result=[]
    def go_ahead(current_path):
        list_path=os.listdir(current_path)
        list_dirs=[x for x in list_path if os.path.isdir(x)]
        list_files=[x for x in list_path if os.path.isfile(x)]
        contain_key=[x for x in list_files if s in os.path.split(x)[1]]
        if contain_key:
            result.append(contain_key)
        for i in list_dirs:
            go_ahead(i)

    go_ahead('.')
    return result

print search('s')
