# -*- coding: utf-8 -*-
import subprocess
import binascii

f=open('param.file.tgz','rb')
out=open('out.txt','r+')   ##输出解码文件
d1={}    ##奇数字典
d2={}    ##偶数字典

def readword(offset):  ##读取值函数
    out.seek(offset)
    while True:
        if out.read(1)==' ':
            offsetend=out.tell()
            break
    out.seek(offset)
    return (out.read(offsetend-offset),offsetend)

for a in range(33,127):    ##生成奇偶字典
    if a+201<256:
        d1.update({(a+201):chr(a)})
    else:
        d1.update({(a-55):chr(a)})
    d2.update({(a+115):chr(a)})

while True:
    word=f.read(1)
    if len(word)==0:
        break
    else:
        word=binascii.b2a_hex(word)
        word2int=int(eval(b'0x'+word))
        offset=f.tell()
        if offset%2==1:
            out.write(d1.get(word2int,' '))
            #print(d1.get(word2int,' '),file=out,end="")
        else:
            out.write(d2.get(word2int,' '))
            #print(d2.get(word2int,' '),file=out,end="")
(AdminName,AdminName_end)=readword(164)
(AdminPass,AdminPass_end)=readword(AdminName_end+11)
print("ID=",AdminName)    ##输出账号ID
print("Pass=",AdminPass)    ##输出账号密码
#subprocess.call("pause",shell=True)