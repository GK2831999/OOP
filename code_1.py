class RealNumber:

    def __init__(self,r=0):
        self.__realValue = r
    def getRealValue(self):
        return self.__realValue
    def setRealValue(self,r):
        self.__realValue = r

    def __str__(self):
        return 'RealPart: ' +str(self.getRealValue())            


class ComplexNumber:
    def __init__(self,r_p = 1.0,I_p = 1.0):
        self.r = r_p
        self.p = I_p
    def __str__(self):
        return f"""RealPart: {self.r}
ImaginaryPart: {self.p}
        """

    


r  = RealNumber(2)

cn1 = ComplexNumber()


print(cn1)


print('-------------------')


cn2 = ComplexNumber(5,7)


print(cn2)