#coding=utf-8
#1.菱形
for i in range(-3,4):
    #print(i)
    if i<0:
        a=abs(i)
    else:
        a=i
    print(' '*a+'*'*(7-a*2))

#2.菱形2
n=int(input('请输入一个数字'))
c=n//2
for i in range(-c,c+1):
    a=-i if i<0 else i
    print(' '*a+'*'*(n-a*2))

#3.圣杯(对顶三角)
print('=='*10)
n=7
e=n//2
for i in range(-e,n-e):
    a=-i if i<0 else i
    print(' '*(e-a)+'*'*(2*a+1))
#4.判断数字大小
print('=='*10)
m=int(input('请输入一个数字'))
while 1:
    n=int(input('请输入下一个数字'))
    if n:
        if n>m:
            m=n
            print('max is ',m)
        else:
            break
#5.99乘法表
#end在格式化输出中表示不换行显示
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end=' ')
    print()
    



