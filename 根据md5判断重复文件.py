import os,shutil
import hashlib


'''
遍历文件夹、根据md5整理非重复文件
'''

#文件md5值集合
md5_set=set()
#遍历文件,并计算md5值
def read_dirs(f_path):
    # 获取f_path路径下的所有文件及文件夹
    paths = os.listdir(f_path)
    # 获得目标文件后复制过去的路径
    target_path = r"H:\小说"
    # 判断
    for f_name in paths:
        com_path = f_path + "\\" + f_name
        print(com_path)
        if os.path.isdir(com_path):  # 如果是一个文件夹
            read_dirs(com_path)    # 递归调用
        if os.path.isfile:    # 如果是一个文件
            try:
                suffix = com_path.split(".")[1]  # suffix=后缀（获取文件的后缀）
            except Exception as e:
                continue    # 对于没有后缀的文件省略跳过
            try:
                # 可以根据自己需求，修改不同的后缀以获得该类文件
                # if suffix == "pdf" or suffix == "PDF":        # 获取pdf文件
                #     shutil.copy(com_path, target_path)
                # elif suffix == "docx" or suffix == "DOCX":    # 获取docx文件
                #     shutil.copy(com_path, target_path)
                # elif suffix == "jpg" or suffix == "JPG":      # 获取jpg文件
                #     shutil.copy(com_path, target_path)
                # elif suffix == "png" or suffix == "PNG":      # 获取png文件
                #     shutil.copy(com_path, target_path)
                # elif suffix == "xlsx" or suffix == "XLSX":    # 获取xlsx文件
                #     shutil.copy(com_path, target_path)
                # elif suffix == "mp4" or suffix == "MP4":      # 获取mp4文件
                #     shutil.copy(com_path, target_path)
                # else:
                #     continue
                if suffix=="txt" or suffix=="TXT":
                    result_md5=hashlib.md5(open(com_path, 'rb').read()).hexdigest()
                    if(result_md5) not in md5_set:
                        md5_set.add(result_md5)
                        shutil.copy(com_path, target_path)

            except Exception as e:
                print(e)
                continue
if __name__ =="__main__":
    f_path=r"J:\小说"
    read_dirs(f_path)
