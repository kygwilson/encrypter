class affine_cipher():
    def __init__(self, message, multiply = 1, add = 0):
        self.message = message
        self.multiply = multiply
        self.add = add

    def encrypt(self):
        self.encrypted = ''

        for character in self.message:
            if character.isupper():
                num = ((((ord(character) - 64)  * self.multiply) % 26) +
                       self.add) % 26
                if num == 0:
                    num = 26
                self.encrypted += chr(num + 64)
            elif character.islower():
                num = ((((ord(character) - 96)  * self.multiply) % 26) +
                       self.add) % 26
                if num == 0:
                    num = 26
                self.encrypted += chr(num + 96)
            else:
                self.encrypted += character

    def get_affine_encrypted(self):
        return self.encrypted

    def decrypt(self):
        """ Expects a string representing a coded affine message
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

        # List of coprimes of 26 (the available options for a Affine Cipher)
        coprimes = [3, 5, 7, 11, 15, 17, 19, 21, 23, 25]

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
        for addition in range(0,26):
            for multiplication in coprimes:
                solution_set = []
                for word in clean_list:
                    tested = self.shift_word(word, multiplication,
                                                   addition)
                    # Check if the tested word is in the dictionary, add if so
                    if tested in words:
                        solution_set.append(tested)
                solutions.append(solution_set)

        self.decrypted = ' '.join(max(solutions, key=len))


    def shift_word(self, word, multiplication, addition):
        builder = ''
        for letter in word:
            if ((((ord(letter) -96) * multiplication) + addition) % 26) > 0:
                builder +=  chr(((((ord(letter) -96) * multiplication) +
                                  addition) % 26) + 96)
            else:
                builder += 'z'
        return builder

    def get_affine_decrypted(self):
        return self.decrypted



