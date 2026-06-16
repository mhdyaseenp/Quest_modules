import unittest

# from calculations import add
# from calculations import reversee,add

from calculations import *



# class TestCalculations(unittest.TestCase):
#     def test_addPositiveNumber(self):             
#         """when we give the name of an test case the name start with test_  """    
"""assertEqual"""    
#         result=add(20,5)
#         self.assertEqual(result,25)
#         # self.assertEqual(add(20,5),25)
        
        
#     def test_add_Negative_Number(self):
#         self.assertEqual(add(-20,-8),-28)
        
        
#     def test_ReverseString(self):
#         self.assertEqual(reversee("yaseen"),'neesay')   
         
        
#     def test_Reverse_Iteger(self):
#         self.assertEqual(integerRev(112),211)   
        
        
#     def test_NegativeReverse_Iteger(self):
#         self.assertEqual(NegativeintegerRev(112),-211)   
        
"""assertRaises"""
#     def test_Division(self):
#         """when we gave the value like(10,5) its show ZeroDivisionError not raise """
#         # self.assertEqual(div(10,5),2)   
#         # self.assertEqual(div(-10,-5),2)   
#         with self.assertRaises(ZeroDivisionError):
#             div(10,0)  
        
    
         
# unittest.main()





"""assertTrue   | assertFalse | assertIn  | assertNotIn"""


class TestLetters(unittest.TestCase):
    def test_uppercase(self):
        self.assertTrue("PYTHON".isupper())
        
        
    def test_lower(self):
        self.assertFalse("python".isupper())
        
        
    def test_mebershop(self):
        fruits = ['apple','banana','orange']
        self.assertIn("apple",fruits)
          
    def test_mebershop2(self):
        fruits = ['apple','banana','orange']
        self.assertNotIn("mango",fruits)
        
        
    def test_none(self):
        self.assertIsNone(get_data())
    
    def test_is(self):
        a=[1,2] 
        b=a
        self.assertIs(a,b)       
        
         
        
    def test_is(self):
        self.assertAlmostEqual(20/3,6.66667,places=3)        
        
        
unittest.main()