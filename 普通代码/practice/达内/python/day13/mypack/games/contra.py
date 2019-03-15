


def play():
    print("正在玩魂斗罗1!!")

def gameover():
    print("魂斗罗游戏结束")
    #调用上一层文件里的menu.py里的show_menu函数
    #方法一 用绝对导入的方式
    # from mypack.menu import  show_menu

    #方法二用相对导入方式
    from ..menu import show_menu
    show_menu() #调用

    #想在此处调用tanks.py里的play函数怎么导入
    #方法一
    # import mypack.games.tanks as tanks
    # tanks.play()
    #方法二
    # from mypack.games.tanks import play()
    # play()
    #方法三
    from .tanks import play
    play()


print("魂斗罗被加载！！！")





