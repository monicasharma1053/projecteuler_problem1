


class NaturalNumber:

    global maxNumber


    def IsDefinedNumber(self, number):
        self.maxNumber=number

    def IsMaxNumberValid(self,maxNumber):
        if maxNumber >= 0:
            return True

    def NaturalNumbers(self, maxNumber):
        return list(range(maxNumber))

    
        
