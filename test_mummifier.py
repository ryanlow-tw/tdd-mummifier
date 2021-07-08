import unittest
from mummifier import Mummifier


class MummifierTest(unittest.TestCase):

    def test_should_return_empty_string(self):
        result = Mummifier().mummify("")
        self.assertEqual("", result)

    def test_should_return_original_string_if_no_vowels(self):
        result = Mummifier().mummify("str")
        self.assertEqual("str", result)

    def test_should_return_a_if_string_is_a_vowel(self):
        result = Mummifier().mummify("a")
        self.assertEqual("mommy", result)


