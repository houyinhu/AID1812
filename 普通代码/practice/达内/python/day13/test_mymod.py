


#此示例示意调用自动定义的mymod.py 模块内的两个函数和两个字符串

import mymod
mymod.myfac(5)
mymod.mysum(100)
print(mymod.name1)

from mymod import name2
print(name2)

from mymod import *
myfac(20)
mysum(1000)



print("test_mymod.py里的__name__属性的值是：",__name__)








