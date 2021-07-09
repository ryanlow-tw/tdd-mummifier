class Mummifier:

    def mummify(self, input_string):
        vowels = ['a', 'e', 'i', 'o', 'u']

        if input_string in vowels:
            return "mommy"
        elif self.vowel_length_is_more_than_30pct(input_string):
            pass
        else:
            return input_string

    def vowel_length_is_more_than_30pct(self, input_string):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = 0

        if len(input_string) == 0:
            return False

        for char in input_string:
            if char in vowels:
                vowel_count += 1
        pct_vowels = vowel_count / len(input_string)
        return pct_vowels > 0.3
