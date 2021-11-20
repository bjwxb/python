# 字符串格式化输出

# 1. 运算符 - % 格式化字符串（d-整数/s-字符串/f-浮点数/x-十六进制）
print("Hello %s World! %d" % ("python", 5))
# 2. 字符串方法format
print("Hello {0} World! {1:.1f}%".format('python', 12.12))
str1 = 'python'
str2 = 133
# 3. f-string格式化
print(f'Hello {str1} world! {str2}')


ret = []
# 循环
for i in range(1, 5):
    if i % 3 == 0:
        continue  # 3 的倍数时跳过本次循环
    ret.append(i)  # 1，2，4符合条件
print(ret)

ret = []
for i in range(1, 10):
    if i % 3 == 0:
        break  # 遇到3 的倍数时退出循环
    ret.append(i)  # 只循环了两次 1和2
print(ret)


def test():
    a = []
    for ii in range(1, 10):
        a.append(ii)
        if ii == 3:  # 当值等于3时 return，等于终止函数运行
            return a


print(test())


# 去除字符串首尾空格
def trim(s):
    st = 0
    length = len(s)
    while st < length and s[st] == ' ':
        st += 1

    while st < length and s[length-1] == ' ':
        length -= 1

    return s[st:length]


if __name__ == '__main__':
    ret = trim("       hello world! ")
    print(f'ret = >>>{ret}<<<{len(ret)}===={ret[:]}')
    # if trim('hello  ') != 'hello':
    #     print('测试失败!1')
    # elif trim('  hello') != 'hello':
    #     print('测试失败!2')
    # elif trim('  hello  ') != 'hello':
    #     print('测试失败!3')
    # elif trim('  hello  world  ') != 'hello  world':
    #     print('测试失败!4')
    # elif trim('') != '':
    #     print('测试失败!5')
    # elif trim('    ') != '':
    #     print('测试失败!6')
    # else:
    #     print('测试成功!')

    a = ()
    b = []
    c = {}
    d = None
    e = 0
    f = ''
    while a or b or c or d or e or f:
        print('---- condition is true ----')
        break
    else:
        print('========== false =====')

    print(type('xyz'))  # 一个字符占若干个字节 string 通过encode转换为bytes
    print(type(b'xyz'))  # 一个字符占一个字节

