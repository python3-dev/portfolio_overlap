import io
import unittest
import unittest.mock

from geektrust import getinput


class test_integration(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        return super().setUp()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_getinput_0(self, mock_stdout):
        with open('test/fixtures/output1.txt', 'r') as f:
            expected_out = f.read()
        getinput('test/fixtures/input1.txt')
        self.assertEqual(mock_stdout.getvalue(), expected_out)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_getinput_1(self, mock_stdout):
        with open('test/fixtures/output2.txt', 'r') as f:
            expected_out = f.read()
        getinput('test/fixtures/input2.txt')
        self.assertEqual(mock_stdout.getvalue(), expected_out)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_getinput_2(self, mock_stdout):
        with open('test/fixtures/output3.txt', 'r') as f:
            expected_out = f.read()
        getinput('test/fixtures/input3.txt')
        self.assertEqual(mock_stdout.getvalue(), expected_out)
