import random

random.seed(11)

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class NameEncoder:
    """ Encode names using Cesar encoding.
    Also embeds the associated decoder function.
    Shifts each character of the name by a given number of letters. """

    def __init__(self, code=3):
        self.code = code

    def encode(self, name):
        return self._shift(name, self.code, ALPHABET, "add")

    def decode(self, name):
        return self._shift(name, self.code, ALPHABET, "substract")

    @staticmethod
    def _shift(name, code, alphabet, direction: str):
        """ direction = add or subtract """

        if direction == "add":
            indices_list = map(lambda c : (alphabet.index(c) + code) % len(alphabet), name)
        else:
            indices_list = map(lambda c : (alphabet.index(c) - code) % len(alphabet), name)
        char_list = map(lambda i : alphabet[i], indices_list)
        return ''.join(char_list)

    @staticmethod
    def _pad(encoded_name, max_length, alphabet):
        pad_length = max_length - len(encoded_name)
        indices_list = [random.randint(0, len(alphabet)-1) for _ in range(pad_length)]
        pad = map(lambda i: alphabet[i], indices_list)
        return encoded_name + ''.join(pad)

    def encode_name(self, name, expected_length):
        return self._pad(self.encode(name), expected_length, ALPHABET)

    def encode_names(self, names):
        """ Encodes a list of names and makes sure that they do have the same output size. """

        max_length = max([len(n) for n in names])
        
        d = dict()
        for name in names:
            print(f"processing {name}")
            d[name] = self.encode_name(name, max_length)
        return d


