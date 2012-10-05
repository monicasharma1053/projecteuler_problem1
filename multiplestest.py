
from multiples import Multiples
import unittest


class MultiplesTest(unittest.TestCase):



    def setUp(self):
        self.m=Multiples()


    def testOneMultiplier(self):
        self.m.IsDefinedMultiplier(5)
        self.assertEqual(5, self.m.multiplier)

    def testOneValidNumberofMultiples(self):
        self.m.ValidNumberOfMultiples(2)
        self.assertEqual(2, self.m.numberOfMultiples)


    def testRangeOfMultiples(self):
        self.m.multiplier=5
        self.m.numberOfMultiples=2
        self.assertEqual([5,10], self.m.MultiplesRange()) 





if __name__ == '__main__':
    unittest.main()
