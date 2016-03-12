"""commands.py in Pycryption"""
import crypt
import prompt


class command(object):
    """listOfCommands = ["help --showing a list of commands", "quit --for quitting the program",
                      "crypt --starts the encryption process"]"""

    def __init__(self, serviceName):
        self.serviceName = serviceName

    @staticmethod
    def help():
        listOfCommands = ["help --showing a list of commands", "quit --for quitting the program",
                            "encrypt --starts the encryption process", "decrypt --starts the decryption process"]
        for c in listOfCommands:
            print c

    @staticmethod
    def quit():
        exit()

    @staticmethod
    def startEncryption():
        print "[WARRING] Pycryption only support basic english!"
        done = False
        while done is not True:
            print "type in what you want to encrypt down below."
            userInput = str(raw_input(">"))
            if userInput == "":
                print "sorry, you did not type something in to the input."
                continue
            else:
                print "Are you sure, you want to encrypt the string? [y/n]"
                processInput = str(raw_input(">"))
                if processInput == "n" or processInput == "N" or processInput == "no" or processInput == "No" or processInput == "NO":
                    print "stopped process."
                    prompt.startPrompt()
                    # just return to prompt....

                elif processInput == "y" or processInput == "Y" or processInput == "yes" or processInput == "Yes" or processInput == "YES":
                    print 1

    @staticmethod
    def startDecryption():
        print 1

    @staticmethod
    def license():
        print "Copyright 2016 Magnus Refsgaard Christoffersen \n\n " \
              "Licensed under the Apache License, Version 2.0 " \
              "(the \"License\"); you may not use this file except \n in compliance with the License. You may obtain a " \
              "copy of the License at \"http://www.apache.org/licenses/LICENSE-2.0\" \n Unless required by applicable law " \
              "or agreed to in writing, software distributed \n under the License is distributed on an \"AS IS\" BASIS, " \
              "WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,\n either express or implied. See the License for the " \
              "specific language governing permissions and limitations under the License."


