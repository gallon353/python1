#coding=utf-8
#设置字符集
#字符集相当于翻译官
#中文字符集常用 GBK2312

#1.直接输出
#数字 123456
#字符串 '123' '扣你七娃'
print('哈勒少！！！！')
print(100)

#2.变量输出
#python程序中所有的符号必须是英文
#变量:可以变化的值，就是一个容器
a='告诉你妈妈晚上不回家，我给你看我写的代码！！'
#a就是变量的名字，等号后面就是变量的值
#print()函数可以对数据和变量的值进行输出
print(a)
a=100
print(a)
#变量操作后输出
a=100
b=20
print(a+b)
a='heygor'
b='handsome!!!'
print(a+b)

#3.函数输出
#系统中会有很多自带函数，可以进行操作
#abs()   绝对值
#len()   长度

print(abs(-20))
s='爱你么么哒！！'
print(len(s))

#4.格式化输出
#  %s  接受变量传回来的字符类型数据
#  %d  接受变量传回来的数字类型数据
#  输出内容如果只有一个变量值不需要加括号，多个一定要加括号
#小红是no.1
#小明是no.2
#小刚是no.3
name='heygor'
num=1
print('%s is no.%d'%(name,num))

name='lilei'
print('my name is %s'% name)

name='simida'
#print('myname is %d '% name)













