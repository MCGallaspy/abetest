# We'll use unittest as an automatic code runner.
import unittest
import functools

# And we'll use mocks to make sure students don't bypass
# question requirements.
import unittest.mock as mock

# The student must supply an answers module!
import answers as ans


class Problem1Key(unittest.TestCase):

    def test_problem_1_returns_True_when_passed_two_ints(self):
        self.assertTrue(ans.problem_1(3, 4))
        
    def test_problem_1_returns_False_when_one_argument_is_not_an_int(self):
        self.assertFalse(ans.problem_1(3, 4.0))


class Problem2Key(unittest.TestCase):

    def test_problem_2_returns_True_when_passed_two_ints(self):
        self.assertTrue(ans.problem_2("3", "4"))
        
    def test_problem_2_returns_False_when_one_argument_is_not_an_int(self):
        self.assertFalse(ans.problem_2("3", "4.0"))


class Problem3Key(unittest.TestCase):

    def test_problem_3_returns_5_when_passed_5(self):
        a, b = ans.problem_3(5)
        self.assertEqual(b, 5)
        
    def test_problem_3_decrements_its_argument(self):
        a, b = ans.problem_3(5)
        self.assertEqual(a, 0)

    def test_that_loop_was_actually_used(self):
        """ We'll use a mock here to assert that the student actually used a loop, by
            checking the call count of some magic methods for arithmetic.
        """
        mock_int = mock.MagicMock()
        mock_val = 5
        
        def mock_iminus(other):
            nonlocal mock_val, mock_int
            mock_val -= other
            return mock_int

        def mock_minus(other):
            nonlocal mock_val, mock_int
            mock_val -= other
            return mock_int
            
        def mock_gt(other):
            nonlocal mock_val
            return mock_val > other

        def mock_eq(other):
            nonlocal mock_val
            return mock_val == other
            
        mock_int.__isub__ = mock.Mock(side_effect=mock_iminus)
        mock_int.__sub__ = mock.Mock(side_effect=mock_minus)
        mock_int.__gt__ = mock.Mock(side_effect=mock_gt)
        mock_int.__eq__ = mock.Mock(side_effect=mock_eq)
        mock_int = functools.total_ordering(mock_int)
        
        ans.problem_3(mock_int)
        counts = [mock_int.__isub__.call_count, mock_int.__sub__.call_count]
        self.assertTrue(any(count == 5 for count in counts))


if __name__ == '__main__':
    unittest.main()