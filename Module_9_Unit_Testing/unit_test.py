import unittest

# from calculations import add
# from calculations import reversee,add

from calculations import *



class TestCalculations(unittest.TestCase):
    def test_addPositiveNumber(self):             
        """when we give the name of an test case the name start with test_. """    
               
        result=add(20,5)
        self.assertEqual(result,25)
        # self.assertEqual(add(20,5),25)
        
        
    def test_add_Negative_Number(self):
        self.assertEqual(add(-20,-8),-28)
        
        
    def test_ReverseString(self):
        self.assertEqual(reversee("yaseen"),'neesay')   
         
        
    def test_Reverse_Iteger(self):
        self.assertEqual(integerRev(112),211)   
        
        
    def test_NegativeReverse_Iteger(self):
        self.assertEqual(NegativeintegerRev(112),-211)   
        
        
    def test_Division(self):
        """when we gave the value like(10,5) its show ZeroDivisionError not raise """
        # self.assertEqual(div(10,5),2)   
        # self.assertEqual(div(-10,-5),2)   
        with self.assertRaises(ZeroDivisionError):
            div(10,0)  
        
        
        
unittest.main()