class Animal :
    def eat(self):
        print('eating')
class Dog(Animal) :
    def bark(self):
        print('barking')

if __name__ == '__main__':
     d = Dog()
     d.eat()
     print(issubclass(Dog,Animal ))
     print(isinstance(d,Dog))
     print(isinstance(d,Animal))