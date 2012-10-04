import unittest



class NaturalNumber: 

    def IsValidNumber(self, number):
        if number >= 0:
            return True 




class IsNaturalNumberTest(unittest.TestCase):


    def testOneIsValidNumber(self):
        naturalnumber = NaturalNumber()
        self.assertTrue(naturalnumber.IsValidNumber(5)) 




if __name__ == '__main__':
    unittest.main()
