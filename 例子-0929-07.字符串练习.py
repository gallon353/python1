#coding=utf-8

name=input('请输入您的文字： ')

if len(name)==0:
    print('您的输入有误')
else:
    if name[0] in 'AEIOUaeiou':
        print(name+'ay')
    else:
        print(name[1:]+name[0]+'ay')        
