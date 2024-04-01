class A:
    def __init__(self,x,y):
        self.__x = x
        self.y = y

    def display(self):
        return self.__b
 #   @property
 #   def x(self):
  #      return self.__x    property생기면 133 출력  클래스 비에서 객체 에이의 은폐속성 옉세스 가능
class B:
    def __init__(self, z=3):
        self.z =z
    def nana(self,x,y):
        a =A(x,x+y)
        return (a.x, a.y, self.z)   #여기서 엑스가 지역변수=x로 정의되면 133출력
                                # a.x 로 정의하면 어드리부트오류
if __name__ == '__main__':
    b = B()
    print(b.nana(1,2))


    #a객체의 은폐속성에 대한 반환 메소드가 없다 . 프로퍼티나 게터,,
    #B가 A의 하위클래스여도 결과동일함.