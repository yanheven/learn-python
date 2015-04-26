__author__ = 'hyphen'

'''

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
'''
import copy
def query_all(q,l):
    count=0
    for i in l:
        flag_all=True
        new_l=copy.deepcopy(i)
        for j in q:
            if flag_all:
                lenth=len(new_l)
                x=0
                if lenth==0:
                    flag_all=False
                    break
                while x<lenth:
                    y=new_l[x]
                    if j!=y and y>j:
                        flag_all=False
                        break

                    new_l.remove(y)
                    lenth-=1
                    if j==y:
                        break

            else:
                break
        if flag_all:
            count+=1
    return count

def query_any(q,l):
    count=0
    for i in l:
        flag_in=False
        new_l=copy.deepcopy(i)
        for j in q:
            if not flag_in:
                lenth=len(new_l)
                x=0
                while x<lenth:
                    y=new_l[x]
                    if j==y:
                        flag_in=True
                        count+=1
                        break
                    elif y>j:
                        break
                    else:
                        new_l.remove(y)
                        lenth-=1
                        x-=1
                    x+=1
            else:
                break

    return count

def query_some(q,l):
    count=0
    for i in l:
        flag_all=True
        flag_in=False
        new_l=copy.deepcopy(i)
        for j in q:
            lenth=len(new_l)
            x=0
            if lenth==0:
                flag_all=False
            while x<lenth:
                y=new_l[x]
                if j!=y and y>j:
                    flag_all=False
                    break
                elif j==y:
                    flag_in=True
                    new_l.remove(y)
                    lenth-=1
                    break
                else:
                    new_l.remove(y)
                    lenth-=1
        if flag_in and not flag_all:
            count+=1
    return count

if __name__=='__main__':
    n=int(raw_input())
    flist=[] #files
    qlist=[] #querys

    for i in range(n):
        fline=str(raw_input()).split(' ')
        fline=map(int,fline[1:])
        fline.sort()
        flist.append(fline)

    q=int(raw_input())
    ret=[]

    for i in range(q):
        qline=str(raw_input()).split(' ')
        qline=map(int,qline)
        t=qline[0]
        k=qline[1]
        count=0
        query=qline[2:]
        query.sort()
        if t==1:
            count=query_all(query,flist)
        elif t==2:
            count=query_any(query,flist)
        elif t==3:
            count=query_some(query,flist)
        ret.append(count)
    for i in ret:
        print(i)


