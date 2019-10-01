class caesar_cipher():
    def __init__(self, message = '', key = 0):
        self.message = message
        self.key = key % 26

    def encrypt(self):
        self.translated = ''

        for character in self.message:
            if character.isalpha():
                num = ord(character)
                num += self.key

                if character.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif character.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26

                self.translated += chr(num)
            else:
                self.translated += character

    def get_caesar_encrypted(self):
        return self.translated

    def decrypt(self):
        """ Expects a string representing a coded caesar message
            Returns a decoded message. """

        # Declares the list Solutions
        solutions = []

        # Opens the dictionary
        with open("dictionary.txt") as dictionary:
            # Creates a set where the lambda i applies to every line
            words = set(map(lambda clean: clean.strip().lower(),
                            dictionary.readlines()))
            # Adds the words "a" and "i" to the set
            words |= set(['a', 'i'])

        # Clean up message by removing spaces, and non-alpha characters
        message_list = self.message.split()
        clean_list = []
        for word in message_list:
            builder = ''
            for letter in range(len(word)):
                if word[letter].isalpha():
                    builder += word[letter].lower()
            clean_list.append(builder)

        # Iterate over all 260 possibilities of multiplication and shifts
        for shift in range(0,26):
            solution_set = []
            for word in clean_list:
                tested = self.shift_word(word, shift)
                # Check if the tested word is in the dictionary, add if so
                if tested in words:
                    solution_set.append(tested)
            solutions.append(solution_set)

        self.decrypted = ' '.join(max(solutions, key=len))


    def shift_word(self, word, shift):
        builder = ''
        for letter in word:
            if (((ord(letter) -96) + shift) % 26) > 0:
                builder +=  chr((((ord(letter) -96) + shift) % 26) + 96)
            else:
                builder += 'z'

        return builder

    def get_caesar_decrypted(self):
        return self.decrypted

x = caesar_cipher("Whvw, wvdpsoh whaw", 5)
x.decrypt()
print(x.get_caesar_decrypted)
