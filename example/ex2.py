# 求[100-1000]之间的水仙花数, 个位数的立方 + 十位数的立方 + 百位数的立方 结果是 个十百 三个数的组合
def daffodil():
    for i in range(100, 1000):
        low = i % 10  # 求出个位数的值
        middle = i // 10 % 10  # 求出十位数的值
        high = i // 100  # 求出百位数的值
        if i == low ** 3 + middle ** 3 + high ** 3:
            print(i)


# 百钱买百鸡，公鸡五元一只/母鸡三元一只/小鸡一元三只
def chicken():
    for x in range(0, 20):  # 公鸡5元最多能买20只
        for y in range(0, 33):  # 母鸡3元最多能买33只
            z = 100 - x - y  # 小鸡数量
            if z % 3 == 0 and x * 5 + y * 3 + z / 3 == 100:
                print(f'x = {x}, y = {y}, z = {z}')
                break


# 输出100以内所有的质数（素数） - 只能被1和自身整除
def prime():
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


# 求10000以内的完美数字 完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
# 例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数
def perfectNum():
    ret = []
    for num in range(2, 10000):  # 遍历
        total = 0  # 记录真因子数的和
        for i in range(1, num):  # 遍历[1，num)
            if num % i == 0:  # 取余判断
                total += i
        if total == num:  # 判断真因子数的和 是否等于  当前num
            ret.append(num)
    print(ret)


if __name__ == '__main__':
    daffodil()
    chicken()
    prime()
    perfectNum()


