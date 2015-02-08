#encoding=UTF-8
__author__ = 'heven'
import os

def process_rename(file_name,file):
    fl=len(file)
    for i in range(fl):
        if "Hyphen" in file[i]:
            file[i]=file[i].replace("Hyphen","海峰 http://weibo.com/344736086")
            break

def get_file_path(path,dir_name):
    file_list=[]
    for i in dir_name:
        files_dir=os.path.join(path,i)
        files= os.listdir(files_dir)
        for j in files:
            file_list.append(os.path.join(files_dir,j))

        #file_list.append(os.path.join(files_dir,(os.listdir(files_dir))))
    return file_list

if __name__=="__main__":
    dir_name=['cloud','thinking','coding']
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.abspath(os.path.join(ROOT_PATH, '../yanheven.github.com/_posts'))
    files=get_file_path(dir_path,dir_name)
    for i in files:
        with open(i,"r") as f:
            file=f.readlines()
        with open(i,'w')as f:
            process_rename((os.path.split(i))[1],file)
            f.writelines(file)
        print("file:%s rename!!\n"%i)
