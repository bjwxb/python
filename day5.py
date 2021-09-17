import logging
logging.basicConfig(level=logging.INFO)
# 异常处理 try...except...finally...
# Exception - 常规错误基类
# ArithmeticError - 所有数值计算错误的基类
# FloatingPointError - 浮点数计算错误
# OverflowError - 数值运算超出最大限制
# ZeroDivisionError - 除0
# AttributeError - 对象没有这个属性
# NameError - 未声明初始化对象/属性
# NotImplementedError - 尚未实现的方法
# TypeError - 对类型无效的操作
# ValueError - 传入无效的参数
#
# debug:
# 1. print 用print()最大的坏处是将来还得删掉它,
# 2. assert 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
# 3. logging 和assert比，logging不会抛出错误，而且可以输出到文件
#    它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
#    当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，
#    debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# 4. pdb
# 5. 设置断点


def test():
    while 1:
        s = input('请输入年龄：')
        try:
            age = int(s)
            if age < 0:
                print('input age wrong!')
            elif age < 10:
                print('>>> 是个小孩')
            elif age < 20:
                print('=== 是个少年')
            elif age < 50:
                print('---- 是个青年人')
            elif age < 100:
                print('>>>> 挺好的')
            else:
                print(">>> 福如东海 寿比南山 <<<")
            break
        except ValueError:  # except 可以根据不同的异常做不同的处理
            pass
        except Exception as e:
            print('except:', e)
        finally:  # 如果定义了finally 不论是否有异常，最后都会执行finally模块
            logging.info(f'******** 肯定会执行 *******{s}')
    pass


if __name__ == '__main__':
    test()
