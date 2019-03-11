import pymysql
f = open("dict.txt")
db = pymysql.connect('localhost','root','123456','dict')

cursor = db.cursor()

for line in f:
    lines = line.split()
    # print(lines)
    word = lines[0]
    password = ' '.join(lines[1:])
    print(password)
    sql = 'insert into words(word,mean)\
        values ("%s","%s")'%(word,password)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("出错")
        db.rollback()
print("执行完毕")
f.close()











