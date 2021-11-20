# 不使用中间变量，交换两个变量a和b的值
def swap():
    a = 5
    b = 10
    a, b = b, a
    print(f'---- a = {a}, b = {b}')


# 反转字符串
def reverse(c):
    a = c[::-1]
    print(a)


if __name__ == '__main__':
    swap()
    reverse("hello world! hah")
