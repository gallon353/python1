#coding=utf-8
import time
def log(i):
    def logwrite():
        print('写入日志1')
        i()
        print('写入日志2')
    return logwrite

@log    #log装饰函数的名字，下面jiaoyi是需要装饰的函数
def jiaoyi():
    print('您的银子减少了')
    time.sleep(1)
    print('他的银子增多了')

f=jiaoyi    #相当于jiaoyi=log(jiaoyi)
f()


