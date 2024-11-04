import unittest
from math_quiz import RandomNumberGen, OperationGen, ProblemGen


class TestMathGame(unittest.TestCase):

    def test_RandomNumberGen(self):

        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = RandomNumberGen(min_val, max_val)
            # Check if the random number is within the specified range
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_OperationGen(self):

        # Test if the operation generated is one of the specified operations
        operations = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of operations
            operation = OperationGen()
            # Check if the operation is one of the specified operations
            self.assertIn(operation, operations)

    def test_ProblemGen(self):
            # Test if the problem and answer generated are correct
            
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (12, 8, '+', '12 + 8', 20),
                (9, 4, '-', '9 - 4', 5),
                (6, 7, '*', '6 * 7', 42),
    
            ]
            # Test a few test cases
            for num1,num2,operator,expected_problem,expected_answer in test_cases:
                problem, answer = ProblemGen(num1, num2, operator)

                # Check if the problem and answer generated are correct
                self.assertEqual(problem,expected_problem)
                self.assertEqual(answer,expected_answer)


if __name__ == "__main__":
    unittest.main()
