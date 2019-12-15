a = int(input("输入一个三位数:"))

a1 = a//100
b1 = (a-a1*100)//10
c1 = a%10
print (a1)
print (b1)
print (c1)

b = (a1**3+b1**3+c1**3)
if a ==b:
    print("yes")
else:
    print("no")
