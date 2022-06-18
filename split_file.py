import re
import os
import shutil
file_path=os.listdir(r"H:\小说")
target_path=r"H:\xs_split"

'''
根据文件名关键字分类小说

'''

pattern_label=".*(玄幻|穿越).*"
for i in file_path:
    result=re.search(pattern_label,i)
    if result:
        label_path=target_path+"\\"+result.group(1)
        if not os.path.exists(label_path):
            os.mkdir(label_path)
        file_absolute_path="H:\\小说"+"\\"+i
        shutil.move(file_absolute_path,label_path)