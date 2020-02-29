import unittest
from tiny_app import *

class MyTests(unittest.TestCase):
   ##your playground starts
   def test_hello(self):
       self.assertEqual(hello(), 'Hello World!')
   ##your playground ends

if __name__=="__main__":
   unittest.main()
