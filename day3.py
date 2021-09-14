class Car:
    def action(self):
        pass


def circle():
    ls = ['java', 'python', 'kotlin']
    for i, v in enumerate(ls):  # list 变成索引-元素对
        print(f'>>> index = {i} >> value = {v}')

    for x, y in [['a', 'A'], ('b', 'B'), {"h": 'hello', 'w': 'world'}]:
        print(x, y)

    print(f'for循环生成list>> {[x * x for x in range(1, 11)]}')
    print(f'for循环条件筛选生成list>> {[x * x for x in range(1, 11) if x % 3 == 0]}')
    print(f"for两层循环生成全排列>> {[m + n for m in 'abc' for n in 'xyz']}")


# 找出列表中的最小数和最大数返回
def findMinAndMax(l):
    if not l:
        return None, None
    if len(l) == 1:
        return l[0], l[0]

    min_v = l[0]
    max_v = l[0]
    for i in l:
        if min_v > i:
            min_v = i
        if max_v < i:
            max_v = i
    return min_v, max_v


if __name__ == '__main__':
    circle()
    if findMinAndMax([]) != (None, None):
        print('测试失败!1')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!2')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!3')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!4')
    else:
        print('测试成功!')
