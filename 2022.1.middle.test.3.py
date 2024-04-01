class Rectangle:
    def __init__(self, width=1, height=1):
        self.__width = width
        self.__height = height

    @property
    def area(self):
        return self.__width*self.__height

if __name__ == '__main__':
    rect = Rectangle(2, 4)
    print(rect.area)