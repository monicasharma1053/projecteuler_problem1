
from multiples import Multiples
import unittest


class MultiplesTest(unittest.TestCase):



    def setUp(self):
        self.m=Multiples()
        self.m.multiplier=5
        self.m.numberOfMultiples=2
        self.m.maxnum=10 


    def testOneMultiplier(self):
        self.m.IsDefinedMultiplier(5)
        self.assertEqual(5, self.m.multiplier)

    def testOneValidNumberofMultiples(self):
        self.m.ValidNumberOfMultiples(2)
        self.assertEqual(2, self.m.numberOfMultiples)


    def testOneRangeOfMultiples(self):
        self.assertEqual([5,10], self.m.MultiplesRange())


    def testOneMultiplesUnderAMax(self):
        self.assertEqual([5,10],self.m.MultiplesUnderAMax(10))


    def testOnefSumOfMultiplesUnderAMax(self):
        self.m.MultiplesUnderAMax(10)
        self.assertEqual(5, self.m.SumOfMultiplesUnderAMax())


    
        
        

        
        
        
        


        





if __name__ == '__main__':
    unittest.main()
