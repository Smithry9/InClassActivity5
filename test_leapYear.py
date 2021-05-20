import unittest
import leapYear

class testCaseAdd(unittest.TestCase):
    #test with normal leap year
    def test_leapYear1(self):
        self.assertEqual(leap(2000), True)
    #test with not a leap year
    def test_leapYear1(self):
        self.assertEqual(leap(1999), False)
    #Negative year
    def test_leapYear1(self):
        self.assertEqual(leap(-30), "Invalid Input Type")
    #Invalid input type
    def test_leapYear1(self):
        self.assertEqual(leap("Hi"), "Invalid Input Type")
    #Test should fail
    def test_leapYear1(self):
        self.assertEqual(leap(2000), False)



if __name__ == "__main__":
    unittest.main()
