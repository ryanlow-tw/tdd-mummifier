class Mummifier:

    def mummify(self, input_string):
        vowels = ['a', 'e', 'i', 'o', 'u']

        if input_string in vowels:
            return "mommy"

        return input_string
