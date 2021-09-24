# 练习题


# lst = [3, 6, 2, 7]
# 这四个数字能组成多少个互不相同且无重复数字的三位数？比如362算一个，326算一个，请逐个输出他们
def ex1():
    lst = [3, 6, 2, 7]
    m = 0
    for i in lst:
        for j in lst:
            if i == j:
                continue
            for k in lst:
                if k == i or k == j:
                    continue
                if i != j and i != k and j != k:
                    m += 1
                    print(f"{m} >> ", i, j, k)


if __name__ == '__main__':
    ex1()
