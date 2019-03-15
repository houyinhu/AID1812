
def get_chinese_chr_count(s):
    count=0#用来记录中文字数
    for x in s:
        if 0x4E00< ord(x) <0x9FA5:
            count+=1
    return count
s=input("请输入一段中英文混合字符串")
print("中文的字符的个数是：",
      get_chinese_chr_count(s))




