class command(object):
    listOfCommands = ["help --showing a list of commands", "quit --for quitting the program", ""]

    def __init__(self, serviceName):
        self.serviceName = serviceName

    def help(self):
        for command in self.listOfCommands:
            print command

    def quit(self):
        exit()




