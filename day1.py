# 1. 打印出[100,200]之间满足如下条件的数字：1. 可以被7整除；2, 不能被5整除
def test():
    for i in range(100, 200):  # rang 包含100 不包含200
        if i % 5 != 0 and i % 7 == 0:
            print(i)


# 2.1 求阶乘 factorial
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


# 2.2 for 循环求阶乘
def fact2(num):
    ret = 1
    if num < 2:
        return ret
    else:
        for i in range(1, num+1):
            ret = ret * i
    return ret


# 3. 斐波那契数列
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


# input: n , output: dict[n] = n * n
def square(num):
    d = {}
    for i in range(1, num+1):
        d[i] = i * i
    print(d)


def covert():
    s = input("请输入字符串，按回车结束输入：")  # python2 - raw_input(string),input(int/float) ; python3 - input(string)
    print(s.upper())  # string.upper 大写
    print(type(s))
    ret = s.split(',')  # split 返回一个list
    print(tuple(ret))  # list 转 tuple


if __name__ == '__main__':
    # test()
    # print(fact2(5))
    # print(fact(5))
    # print(fibonacci(3))
    # square(5)
    # covert()
    x = [3, 5, 7]
    x[1:] = [2, 8, 8, 9]
    x[1] = (3,)
    x[2] = 2
    # print(x[1])
    # print(x)
    print(x[1:4])
    # for i in x:  # 3, (3, 4), 2, 8, 9,
    #     print(i, end=', ')
    # print('abc'.encode('ascii'))
    # print(b'abc'.decode('ascii'))
    # print("你好".encode('utf-8'))  # utf-8
    # print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8'))
    print(f"Hello %s World! {x}" % "java")
