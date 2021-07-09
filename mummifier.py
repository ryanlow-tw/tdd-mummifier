class Mummifier:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def mummify(self, input_string):

        if input_string is None:
            raise TypeError("Please input a valid string!")

        input_string = input_string.lower()

        if self.vowel_length_is_more_than_30pct(input_string):
            return self.replace_vowel_with_mommy(input_string)
        else:
            return input_string

    def vowel_length_is_more_than_30pct(self, input_string):

        vowel_count = 0

        if len(input_string) == 0:
            return False

        for char in input_string:
            if char in self.vowels:
                vowel_count += 1
        pct_vowels = vowel_count / len(input_string)
        return pct_vowels > 0.3

    def replace_vowel_with_mommy(self, input_string):
        result_string = ""
        is_vowel = None
        for i in range(len(input_string)):
            char = input_string[i]
            if char in self.vowels:
                is_vowel = True
                end_of_string = len(input_string) - 1
                if i == end_of_string:
                    result_string += 'mommy'
                    return result_string
            else:
                if is_vowel:
                    result_string += 'mommy'
                    is_vowel = False
                result_string += char
        return result_string
