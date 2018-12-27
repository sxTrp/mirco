#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-27 下午1:20
# @Author  : ShaoXin
# @Summary :
# @Software: PyCharm
import threading


class KThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False

    def start(self):

        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run  # Force the Thread to install our trace.
        threading.Thread.start(self)

    def __run(self):
        """Hacked run function, which installs the
        trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True


def time_limit(interval, callback_return):
    """
    函数超时换回
    :param interval:超时时间
    :param callback_return:超时返回结果
    :return:
    """
    def to_do(func):
        def _new_func(old_func, result, old_func_args, old_func_kwargs):
            result.append(old_func(*old_func_args, **old_func_kwargs))

        def deco(*args, **kwargs):
            result = []
            new_kwargs = {  # create new args for _new_func, because we want to get the func return val to result list
                'old_func': func,
                'result': result,
                'old_func_args': args,
                'old_func_kwargs': kwargs
            }
            thd = KThread(target=_new_func, args=(), kwargs=new_kwargs)
            thd.start()
            thd.join(interval)
            alive = thd.isAlive()
            thd.kill()  # kill the child thread
            if alive:
                print('func %s run time out of %s' % (func.func_name, interval))
                return callback_return
            else:
                return result[0]
        return deco
    return to_do

if __name__ == '__main__':
    pass
