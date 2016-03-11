"""prompt.py in Pycryption"""


def startPrompt():
    # mmm
    crash = False
    while crash != True:
        input = str(raw_input(">"))
        if input == "":
            print "Remember to write something before hitting ENTER."
            continue
        elif input == "quit":
            quit()
            crash = True
            # bye bye
        elif input == "help" or input == "?":
            help()

