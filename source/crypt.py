"""crypt.py in Pycryption"""


class crypt(object):
    cList = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5',
                '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', "\"", ']', '^', '_', '`', 'a',
                'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z', '{', '|', '}', '~']  # in total 95 characters long!
    nList = []  # made automatic in __init__ 1-95

    def __init__(self, name):
        self.name = name
        for n in range(1, 96):
            self.nList.append(n)

    @staticmethod
    def encrypt(eInput):
        print eInput


"""  # testing crypt class
c = crypt("test")
print c.nList
"""
