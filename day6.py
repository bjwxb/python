import re
# 正则表达式是一个特殊的字符序列，它能检查一个字符串是否与某种模式匹配
# + 匹配一次或多次
# * 匹配0次或多次
# ？ 匹配0次或1次
# . 匹配除换行符 \n 之外的任何单字符， 使用需转义：\.
# {n} 匹配确定的n次
# {n,} 匹配至少n次
# {n,m} 匹配最少n，最多m次
# [abc] 匹配中括号中所有字符
# [^abc] 匹配除了【】中所有字符
# [a-z] 区间
# \d 匹配一个数字，相当于[0-9]
# \D 匹配一个非数字，相当于[^0-9]
# \w 匹配包括下划线的任何单词字符。等价于[A-Za-z0-9_]
# \W [^A-Za-z0-9_]
# \s 匹配任何空白字符 [ \f\n\r\t\v]
# \S [^ \f\n\r\t\v]
# \n 匹配换行符
# [0-9a-zA-Z\_] 可以匹配一个数字、字母或者下划线
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]* 可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束。

"""
1. re.match(pattern, string, flags=0) 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
        pattern 匹配的正则表达式
        string 要匹配的字符串
        flags 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
        
2. re.search(pattern, string, flags=0)  扫描整个字符串并返回第一个成功的匹配，匹配成功re.search方法返回一个匹配的对象，否则返回None。

3. re.sub(pattern, repl, string, count=0, flags=0) 检索和替换
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
    
4. re.compile 用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用

5. group()???
"""

def testMatch():
    s = "www.baidu.com"
    print(re.match('www', s))  # 匹配成功，返回re.Match对象
    print(re.match('www', s).span())  # (0, 3)
    print(re.match('wwww', s))  # 匹配失败，返回None
    print(re.match('com', s))  # 因为match是从起始位置开始匹配的，所以匹配失败，返回None

    tel = '010-4275893'
    p = r'\d{3}-\d*'
    ret = re.match(p, tel)
    print(ret.span())


def testSearch():
    s = 'www.baidu.com hello world www.site.com '
    print(re.search('www', s).span())
    print(re.search('com', s).group())
    print(re.search('com', s).span())


def testSub():
    phone = "2004-959-559 # 这是一个国外电话号码"

    # 删除字符串中的 Python注释
    # num = re.sub(r'#.*$', "", phone)  # 1.直接re.sub 匹配
    pattern = re.compile(r'#.*$')  # 2.生成正则表达式 匹配
    num = pattern.sub('', phone)
    print("电话号码是: ", num)

    # 删除非数字(-)的字符串
    num = re.sub(r'\D', "", phone)
    print("电话号码是 : ", num)


if __name__ == '__main__':
    # testMatch()
    testSearch()
    testSub()
