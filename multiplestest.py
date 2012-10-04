
from multiples import Multiples
import unittest


class MultiplesTest(unittest.TestCase):



    def setUp(self):
        self.m=Multiples()


    def testOneFourMultiplesRange(self):
        self.assertEqual([1,2,3,4], self.m.MultiplesInARange(1,4)) 






if __name__ == '__main__':
    unittest.main()
