def bubble(value):
    #外层循环：对应走访数据的次数
    for i in range(len(value)-1):
        
        #设置数据交换的标识
        flag = False

        #内层循环：对应每次走访数据时，相邻数据对比次数
        for j in range(len(value)-1-i):
            #要求从低到高
            #若次序有无则交换
            if value[j] > value[j+1]:
                value[j],value[j+1] = value[j+1],value[j]
                
                #更改数据交换标识
                flag = True
        #若未发生数据交换，则说明后续数据均有序
        #跳出数据走访
        if flag == False:
            break

    #走访数据次数
    print("走访次数：",i+1)


if __name__ == '__main__':
    #原始数据value
    value = [300,1, 4, 5, 54, 65, 65, 465, 465, 564, 564, 654, 4654]
    bubble(value)
    print(value)


