#coding=utf-8

class student:                 #创建一个类
    def study(self):           #方法列表
        print('im study!!!')   #方法列表中的逻辑
    def play(self):
        print('play ball')

boy=student()
#产生一个student对象，通过boy实例对象来访问属性和方法
boy.age=20
#给对象添加属性，注意，如果在后面再次出现，表示对属性进行修改
boy.favor='baseball'

#实例化对象boy调用类里面的方法
boy.study()
boy.play()

print(boy.age)
print(boy.favor)

#注意:创建一个对象可以理解为用模型创造实物
