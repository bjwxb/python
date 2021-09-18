import os
# file使用
"""
File 对象方法: file 对象提供了操作文件的一系列方法。
OS 对象方法: 提供了处理文件及目录的一系列方法。

先用Python内置的open()函数打开一个文件，创建一个file对象，然后用file相关的方法才可以对文件进行读写
file object = open(file_name [, access_mode][, buffering])
    file_name：是一个包含了你要访问的文件名称的字符串值。
    access_mode：决定了打开文件的模式：只读，写入，追加等。这个参数是非强制的，默认文件访问模式为只读(r)。
    buffering:  如果buffering的值被设为0，就不会有寄存。
                如果buffering的值取1，访问文件时会寄存行。
                如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。
                如果取负值，寄存区的缓冲大小则为系统默认。

    1. open - r(只读)/r+(可读可写)/w（可写可创建可覆盖）/w+(可读，写，创建，覆盖)/a（追加-可写/可创建）/a+(追加-可读可写可创建)
    2. write/writelines
    3. read/readline/readlines
    4. close
    5. 文件定位
        tell - 方法告诉你文件内的当前位置
        seek - 改变当前文件的位置
    6. flush - 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入
    os模块提供了执行文件处理操作的方法：
    1. rename - os.rename(current_file_name, new_file_name)  重命名
    2. remove - os.remove(file_name) 删除一个文件
    3. mkdir - os.mkdir("new_dir") 创建一个新目录
    4. chdir - chdir()方法来改变当前的目录
    5. getcwd - 显示当前的工作目录
    6. rmdir - 删除目录，目录名称以参数传递

"""


def test():
    f = open('file.text', 'a+')
    print('file name', f.name)  # 文件名字
    print('file isClosed', f.closed)  # 文件是否关闭，false时可以写入
    print('file mode is', f.mode)  # 文件打卡的模式（读/写/创建/覆盖/追加等）
    f.write(' hello world ')
    f.writelines('nice to meet you \n hah \n oh my god')
    f.flush()  # 刷新缓冲区
    print(f'文件当前位置：{f.tell()}')
    f.seek(0)  # 移动指针
    print(f'移动后文件当前位置：{f.tell()}')
    print(f">>> 读取文件内容 = {f.read(12)}")
    print('==================')
    f.seek(7)
    # 读取指定位置后的所有内容
    print(f.read())
    f.close()  # 刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入
    print('file isClosed', f.closed)


def test2():
    f = open('tt.log', 'w')
    f.close()
    # os.rename('tt.log', 'tt.md')
    os.remove('tt.log')
    # os.mkdir('hello')
    os.rmdir('hello')


if __name__ == '__main__':
    test()
    # test2()
