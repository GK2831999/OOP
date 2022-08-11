class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name

        def getName(self):
            return self.name

        def hasFormalin(self):
            return self.__formalin
class Mango:
    def getName(self):
        return "Mango"
    def hasFormalin(self):
        return True

    def __str__(self):
        return "Mangos are bad for you"
class Jackfruit:
    def getName(self):
        return "Jackfruit"
    def hasFormalin(self):
        return False      
    def __str__(self):
        return "Jackfruits are good for you"      
class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the',f.getName(),'.')
            print(f)
        else:
            print('Eat the',f.getName(),'.')
            print(f)

m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)