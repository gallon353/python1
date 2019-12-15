#coding=utf-8
#python操作mysql需要导入pymysql模块
import pymysql
#定义一个mysql的链接参数
conn=pymysql.connect(
    host='localhost',  #链接的主机名或者IP地址
    user='root',       #链接时候使用的用户名
    passwd='root',     #链接时候使用的密码
    db='test',         #链接时候使用的数据库
    port=3306,         #链接时候的端口
    charset='utf8'     #字符集
    )
#打开游标
cur=conn.cursor()
#所需要执行的语句
cur.execute('select * from test1')
#获取SQL语句的执行结果
data=cur.fetchall()
#print(data)
for i in data:
    print(i)
#操作完毕后要关闭游标
cur.close()
#关闭数据库链接
conn.close()



