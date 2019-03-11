#with.py



class A:    #自定义资源管理器
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print("__enter__方法被执行")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被执行')
        if exc_type is None:    #没有异常
            print('没有异常')
        else:#出现异常
            print('错误类型：exc_type')
            print('错误对象：exc_val')
            print('TrackBack：exc_tb')


if __name__ == "__main__":
    with A('练习') as a :
        print('with语句执行了')
        a = int(input("请输入数字，输入别的会报错")) #制造或不制造异常

        print("程序退出")








