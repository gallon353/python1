#coding=utf-8
#计算一个函数的运行时间
import time
def jisuan(func):
    def zsq():
        starttime=time.time()        #函数执行前开始时间
        func()                       #执行函数
        endtime=time.time()          #函数执行后时间
        sec=endtime-starttime        #获取时间差
        print('函数的运行时间为%.6s'% sec)
    return zsq
@jisuan                              #@xxx下面是被装饰的函数
def func():
    print('hello')
    time.sleep(1)
    print('world')

f=func
f()
    
