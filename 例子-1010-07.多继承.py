#coding=utf-8

class a:
    def PrintA(self):
        print('----a-----')

class b(a):
    def PrintB(self):
        print('---b----')

class c(b):   #c类从a和b类中继承，可以调用a和b类中的属性和方法
    def PrintC(self):
        print('---c----')

c1=c()
c1.PrintA()
c1.PrintB()
c1.PrintC()
    
