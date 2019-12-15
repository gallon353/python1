#coding=utf-8

class user:
    def __init__(self,name,passwd,desc):
        self.name=name
        self.passwd=passwd
        self.desc=desc

class super(user):
    quanxian=['z','s','g','c']

class normal(user):
    quanxian=['c']

a=super('heygor','123','帅')
print(a.name)
print(a.desc)
for i in a.quanxian:
    print('数据库操作权限有：'+i)

b=normal('baigor','456','chou')
print(b.quanxian)




