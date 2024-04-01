class Person:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)

if __name__ == '__main__':
    p1= Person("baekhyun")
    p2 = Person("juyeon")
    p1.printName()