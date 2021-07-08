import unittest
from mummifier import Mummifier


class MummifierTest(unittest.TestCase):

    def test_should_return_empty_string(self):
        result = Mummifier().mummify("")
        self.assertEqual("", result)

    def test_should_return_original_string_if_no_vowels(self):
        result = Mummifier().mummify("")
        self.assertEqual("", result)

