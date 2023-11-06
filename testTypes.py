import unittest
import typesOfVariables

class TestsForVariableTypes(unittest.TestCase):
    def testType_python1(self):
        self.assertIsInstance(typesOfVariables.python1, int) # should fail as python1 is a string
    
    def testType_python2(self):
        self.assertIsInstance(typesOfVariables.python2, int) # should pass
    
    def testType_python3(self):
        self.assertIsInstance(typesOfVariables.python3, int) # should fail as python3 is a float

if __name__ == '__main__':
    unittest.main()