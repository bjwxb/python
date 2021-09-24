import _thread as thread
import time

# 多线程
# 线程使用需要导入 thread 模块


"""
1. thread.start_new_thread (function, args[, kwargs] )
    function - 线程函数
    args - 传递给线程函数的参数,他必须是个tuple类型
    kwargs - 可选参数
"""


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f'thread_name = {thread_name}, {time.ctime(time.time())}')


if __name__ == '__main__':
    try:
        thread.start_new_thread(print_time, ('thread_1', 4))
        thread.start_new_thread(print_time, ('thread_2', 6))
    except:
        print('=========')
    while 1:
        pass
