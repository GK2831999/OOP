class RealNumber:
    def __init__(self, number = 0):
        self.number = number 

    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)


class ComplexNumber:
    def __init__(self,n1,n2):
            
        self.n1 = n1
        self.n2 = n2
       
    def __add__(self,anotherNumber):

        return f"{self.n1 +anotherNumber.n1}+{self.n2+anotherNumber.n2}i"

    def __sub__(self,anotherNumber):

        return f"{self.n1 -anotherNumber.n1}-{abs(self.n2-anotherNumber.n2)}i"


    def __str__(self):
        return f"{self.n1}+{self.n2}i"


r1 = RealNumber(3)
print(r1)
r2 = RealNumber(5)

print(r1+r2)
r3 = r1+r2

print(r3)
cn1 = ComplexNumber(2,1)

print(cn1)

cn2 = ComplexNumber(r1.number,5)

print(cn2)


cn3 = cn1 + cn2 


print(cn3)

cn4 = cn1 - cn2
print(cn4)
