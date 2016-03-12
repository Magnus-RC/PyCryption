"""commands.py in Pycryption"""
import crypt


class command(object):
    listOfCommands = ["help --showing a list of commands", "quit --for quitting the program",
                      "crypt --starts the encryption process"]

    def __init__(self, serviceName):
        self.serviceName = serviceName

    @staticmethod
    def help(self):
        for c in self.listOfCommands:
            print c

    @staticmethod
    def quit(self):
        exit()

    @staticmethod
    def crypt(self):
        crypt.startEncryption()



