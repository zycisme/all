import copy
import os
import re

#删除文件名中的汉字，就这样
path=os.getcwd()
file_list=os.listdir(path)
for f in file_list:
    tmp=copy.deepcopy(f)
    old_name=path+"\\"+f
    tmp=re.sub('[一-龥]','',tmp)
    new_name=path+"\\"+tmp
    os.rename(old_name,new_name)
    print(new_name)