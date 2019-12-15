#coding=utf-8
class student:
    def __init__(self,name):
        self.name=name
    def info(self):
        print('你的名字是%s'%self.name)

def StudentInfo(s):
    s.info()
    
#s是形参，必须要传入一个参数，传入参数可以传入实例化对象
heygor=student('gaga')
#heygor是student类的实例化对象
#对象实例化后可以调用类的方法
#heygor.info()

StudentInfo(heygor)
#StudentInfo括号中传入的heygor是一已经实例化的对象，可以调用类的方法
#注意:函数传参可以传入常规数据，也可以传入对象
'''


