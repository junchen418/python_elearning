__author__ = "Damon"
#可知道直接作用于for循环的数据可以：
#1.集合类数据类型，list，tuple，dict，set，str等
#2.generator  包括生成器和带yield的generator function
#这些都直接可以作用于for循环的对象统称为：Iterable 可以使用isinstance（） 判断一个对象是否是Iterable对象
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
import sys
print(sys.argv[0])
#当我们在命令行运行模块文件时，Python解释器把一个特殊变量__name__职位__main__,而在其他地方导入该Hello模块时候，if判断将判断失败，因此，这种if测试
#可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
#序列的新增

