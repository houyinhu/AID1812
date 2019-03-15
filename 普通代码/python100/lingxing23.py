
# 题目：打印出如下图案（菱形）:
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

for i in range(1,5):
    print(' '*(4-i),'*'*(2*i-1))
for i in range(0,3):
    print(' '*(i+1),'*'*(4-(2*i-1)))

print('   *')
print('  ***')
print(' *****')
print('*******')
print(' *****')
print('  ***')
print('   *')

