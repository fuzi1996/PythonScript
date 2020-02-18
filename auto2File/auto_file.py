import os
import datetime
"""
不支持文件名包含中文的文件
"""
# 要复制的目录
path = "D:\\Text"
cmd = "copy "
# 复制到一号机对应目录
out = " y:\输出物提交处\XXX\\test"

list = []
def copy_file(list):
    for i in list:
        if is_today(os.stat(i).st_mtime):
            os.system(cmd+i+out)
            print(cmd+i+out)
def list_all_file(path):
    for i in os.listdir(path):
        if is_file_or_dir(os.path.join(path,i)) == 1:
            list.append(os.path.join(path,i))
        elif is_file_or_dir(os.path.join(path,i)) == 2:
            list_all_file(os.path.join(path,i))

def is_file_or_dir(absolute_path):
    """
    :param absolute_path:
    :return: retrun 1 if it's a file,return 2 if it's a dir
    """
    if os.path.isdir(absolute_path):
        return 2
    elif os.path.isfile(absolute_path):
        return 1

def is_today(tim):
    """
    :param tim: type(tim) is time.struct_time ,is a timestamp,
            os.stat(absolute_path).st_mtime
    :return: if istoday by date return Ture else False
    """
    date_now = datetime.datetime.now().date()
    date = datetime.datetime.fromtimestamp(tim).date()
    if date == date_now:
        return True
    return False


if __name__ == "__main__":
    list_all_file(path)
    copy_file(list)