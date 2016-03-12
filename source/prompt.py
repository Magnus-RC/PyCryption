"""prompt.py in Pycryption"""
import commands


def startPrompt():
    # mmm
    c = commands.command("prompt")
    t = True
    crash = False
    print "please type help to see all the commands"
    while crash is not True:
        cinput = str(raw_input(">"))
        if cinput == "":
            print "Remember to write something before hitting ENTER."
            continue
        elif cinput == "quit":
            print "Good bye. hope you enjoyed the program."
            c.quit()
            crash = True
            # bye bye
        elif cinput == "help":
            c.help()

        elif cinput == "encrypt":
            c.startEncryption()
        elif cinput == "decrypt":
            c.startDecryption()
        elif cinput == "license":
            c.license()
        else:
            print "sorry I did not get that: ", cinput
