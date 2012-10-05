



class Multiples: 

    global numberOfMultiples
    global multiplier
    global multiplicand
    

    def MultiplesInARange(self, multiplier, numberOfMultiples):
        multiplicand=1
        multipleslist = list() 
        while(multiplicand<numberOfMultiples):
            product=multiplier*multiplicand
            multipleslist.append(product+1) 
            multiplicand+1
        return product



    def IsDefinedMultiplier(self, number):
        self.multiplier=number

    def ValidNumberOfMultiples(self, number):
        self.numberOfMultiples=number

    def MultiplesRange(self):
        multiplicand=1
        a =[] 
        while(multiplicand <= self.numberOfMultiples):
            a.append(self.multiplier*multiplicand)
            multiplicand=multiplicand+1
        return a
            


    

    
        


    
        
