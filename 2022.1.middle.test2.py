class X:
    orange = 0
    def __init__(self):
        X.orange +=1
class Y:
    def __init__(self):
        self.banana = 1
    def add(self):
        x=X()
        print(f'{self.banana},{x.orange}')

if __name__ =='__main__':
    y = Y()
    y.add()