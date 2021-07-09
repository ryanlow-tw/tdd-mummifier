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

    def test_should_return_a_if_string_is_a_vowel_e(self):
        result = Mummifier().mummify("e")
        self.assertEqual("mommy", result)

    def test_should_not_replace_vowel_with_mommy_if_vowel_is_less_than_30pct_of_string(self):
        result = Mummifier().mummify("blah")
        self.assertEqual("blah", result)

    def test_should_replace_vowels_with_mommy_if_vowels_are_more_than_50pct_of_string(self):
        result = Mummifier().mummify("blaah")
        self.assertEqual("blmommyh", result)

    def test_should_replace_vowels_with_mommy_if_vowels_are_more_than_50pct_of_string_and_string_ends_with_vowel(self):
        result = Mummifier().mummify("blaa")
        self.assertEqual("blmommy", result)

    def test_if_vowels_are_more_than_50pct_of_string_and_there_are_multiple_set_of_vowels(self):
        result = Mummifier().mummify("blaaha")
        self.assertEqual("blmommyhmommy", result)