class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 2

    def display(self):
        return self.__b

    @property
    def b(self):
        return self.__b


if __name__ =='__main__':
    obj = Demo()
    print(obj.__b) # property사용시 __b g하면 오류뜬다. 'Demo' object has no attribute '__b'

    #b가 은폐였다면 객체외부인 obj에서 엑세스불가
    # init에서 매개변수 정의가 필요없다 이미 지정값이니까 초기화 불필요