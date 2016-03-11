"""prompt.py in Pycryption"""


def cmd():
    # mmm
    crash = False
    while crash != True:
        input = str(raw_input(">"))
        if input == "":
            print "Remember to write something before hitting ENTER."
            continue
        elif input == "quit" or input == "exit":
            crash = True
            # bye bye
        elif input == "help" or input == "?":
            help()

