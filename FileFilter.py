import os
import shutil
import tkinter
from tkinter import filedialog

# 变量
COUNT_LINES = True  # 是否统计行数
COPY_FILE = False  # 是否复制文件
extlist = [".cpp", ".c", ".v", ".h", ".md", ".pdf"]
countlist = [".cpp", ".c", ".v", ".h"]
counter = 0  # 统计行数

# functions
def count_lines(fname):
    count = 0
    for file_line in open(fname, mode="rb"):  # Debug:打不开GBK编码文件，二进制模式开
        # Tips:open返回一个file对象，它是可迭代的，迭代方式是按行迭代
        if file_line != '' and file_line != '\n':  # 过滤掉空行
            count += 1
    print(fname + ':', count)
    return count


# main
# GUI界面

root = tkinter.Tk()
root.withdraw()  # 隐藏多余的窗口
# 选择目标文件夹
sourcePath = filedialog.askdirectory(title='请选择需要操作的文件夹：')
# blacklist = filedialog.askopenfilename(title="请选择需要忽略的文件夹，可多选。不需要忽略文件夹关闭窗口即可。", initialdir=sourcePath , multiple=True)
# 选择备份路径
if COPY_FILE:
    targetPath = filedialog.askdirectory(title="请选择备份的目标路径：")


# 遍历文件夹
for curDir, dirs, files in os.walk(sourcePath):
    for file in files:
        #if curDir in blacklist:
        #    break
        filepath = curDir + "\\" + file
        (name, ext) = os.path.splitext(filepath)  # 分裂拓展名。可以用str.split(.)[-1]替代
        if ext in extlist:  # 查找拓展名列表
            if COUNT_LINES and ext in countlist:
                counter += count_lines(filepath)
            if COPY_FILE:
                path1 = targetPath + "\\" + curDir.split(sourcePath)[-1]  # Warning：如何处理分支？
                if not os.path.exists(path1):  # 判断是否存在文件夹如果不存在则创建为文件夹
                    os.makedirs(path1)
                shutil.copy(filepath, path1)
print("总行数：" + str(counter))
