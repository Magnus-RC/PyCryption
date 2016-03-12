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
    def quit():
        exit()

    @staticmethod
    def crypt():
        crypt.startEncryption()

    @staticmethod
    def license():
        print "Copyright 2016 Magnus Refsgaard Christoffersen " \
              "Licensed under the Apache License, Version 2.0 " \
              "(the \"License\"); you may not use this file except in compliance with the License. You may obtain a " \
              "copy of the License at \"http://www.apache.org/licenses/LICENSE-2.0\" Unless required by applicable law " \
              "or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, " \
              "WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the " \
              "specific language governing permissions and limitations under the License."


