#coding=utf-8
class dog:
    def __init__(self,name,color='black'):
        self.name=name
        self.color=color
    def run(self):
        print('狗富贵，互相旺！')

class taidi(dog):                #继承dog类，可以使用dog类中的属性和方法
    def set_name(self,name):
        self.name=name
    def eat(self):
        print('im eating!!!')

gou=taidi('taitan')
print('名字是%s'%gou.name)
gou.eat()
gou.set_name('2ha')
print('旺财的新名字%s'%gou.name)
gou.run()


