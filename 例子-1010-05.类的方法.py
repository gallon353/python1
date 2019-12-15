#coding=utf-8
'''
class people:
    country='China'
    @classmethod
    def getcountry(cls):
        return cls.country
p=people()
#通过实例对象调用类的方法
print(p.getcountry())
#通过类对象调用类的方法
print(people.getcountry())
'''
#类的方法可以对类的属性进行修改
class people:
    country='China'
    @classmethod
    def GetCountry(cls):
        return cls.country
    @classmethod
    def SetCountry(cls,country):
        cls.country=country

p=people()
print(p.GetCountry())
p.SetCountry('England')
print(p.GetCountry())







