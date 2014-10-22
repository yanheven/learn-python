__author__ = 'hyphen'
class Test():
    i=0
    def __init__(self,x):
        self.i=x

    @classmethod
    def f1(cls):
        print("classmethod")
        print(cls)
        print()

    @staticmethod
    def f2():
        print("statcimethod")

if __name__=="__main__":
    t=Test(1)
    t.f1()
    t.f2()
    Test.f1()
    Test.f2()