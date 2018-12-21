__author__ = "Damon"
#函数的定义   def 函数名 （）  位置参数  默认参数   位置参数必须在默认参数之前显示
#可变参数的使用
#关键字参数的使用

def changeParams(*args):
    for i in args:
        print(i)

if __name__ == '__main__':
    lsit_1 = [1,2,3,4,5,56]
    changeParams(*lsit_1)