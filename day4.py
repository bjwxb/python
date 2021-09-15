from enum import Enum, unique

# 对象练习
"""
1. 类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
2. 单下划线，双下划线，头尾双下划线
    _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
    __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了
    __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
"""


@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Gender(Enum):
    male = '男',
    female = '女',


# 人类
class Person(object):  # 默认继承object，（object）可省略
    __slots__ = ('name', 'gender', "prop")  # 来限制该class实例能添加的属性, 子类不受影响

    # 构造方法， 或成为初始化方法
    def __init__(self, name, gender):
        self.prop = 'person'
        self.name = name
        # self.__gender = gender  # 私有属性
        self.gender = gender  # 限制属性

    # 吃东西
    def eat(self, food='hah'):  # 参数可以设置默认属性
        print(f'{self.gender}======{self.name} eat {food}')

    # 获取性别
    def get_gender(self):
        return self.gender

    # 设置性别
    def set_gender(self, gender):
        self.gender = gender

    # 获取名字
    def get_name(self):
        return self.name

    def print(self):
        print(f'{self.prop}>>>My name is {self.name}, sex is {self.gender}')

    def prt_info(self):
        print('************ class info start ************')
        print(f'class name is {self.__class__}')
        print(f'类的属性： {self.__dict__}')
        print(f'类的文档字符串： {self.__doc__}')
        print(f'类定义所在的模块： {self.__module__}')
        print(f'类的所有父类构成元素： {self.__slots__}')
        print('************* end *******************')


class Chinese(Person):  # 继承
    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.prop = 'Chinese'  # 重写父类属性


class American(Person):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.prop = 'American'

    def print(self):  # 重写父类方法
        print(f'=== I am {self.prop}')


if __name__ == '__main__':
    p = Person('Lucy', '女')
    p.eat('apple')
    p.name = "Jack"
    # p.family = '夹克衫'  # 错误，slots限制了Person的属性
    p.set_gender(Gender)
    print(f'{p.get_name()}  >> {p.get_gender()}')

    print(f">>> {type(p)} >>>")  # types 可判断对象是否是方法/lambda等

    c = Chinese('Ruby', '女')
    c.family = 'HeBei'
    c.print()
    print(isinstance(c, Person))  # 判断一个变量是否是某个类型
    print(hasattr(c, 'name'))  # 判断对象a是否有属性 name
    print(f"get attr name value is >>> {getattr(c, 'name')}")  # 获取不存在的属性会报错AttributeError

    a = American('hah', 'nv')
    a.print()
    a.eat()

    a.prt_info()
