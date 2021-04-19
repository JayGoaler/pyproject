import numpy as np


# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg):
    desktop_path = "C:\\Users\\JayGoal\\Desktop\\新建文件夹\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    # msg也就是下面的Hello world!
    file.write(msg)
    # file.close()


if __name__ == '__main__':
    # 全年每月数据存放在单独的excel表中
    for i in np.arange(1, 32):
        # 调用函数创建一个名为mytxtfile的.txt文件，并向其写入Hello world!
        fileName = 'mytxtfile-' + str(i)
        text_create(fileName, 'Hello world!')
