class Test:
    def __init__(self, a='hello'):
        self.a =a
    def display(self):
        print(self.a)
if __name__=='__main__':
    o = Test()
    o.display()