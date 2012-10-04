
from naturalnumber import NaturalNumber
import unittest




class IsNaturalNumberTest(unittest.TestCase):


    def setUp(self):
        self.n=NaturalNumber()

    def testOneMaxNumber(self):
        self.n.IsDefinedNumber(10) 
        self.assertEqual(10, self.n.maxNumber)

    def testOneIsMaxNumberValid(self):
        self.assertTrue(self.n.IsMaxNumberValid(15))


    def testOneNaturalNumberRange(self):
        self.assertEqual([0,1,2,3], self.n.NaturalNumbers(4)) 
        



if __name__ == '__main__':
    unittest.main()
