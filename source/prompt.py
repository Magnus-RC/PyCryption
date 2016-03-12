"""prompt.py in Pycryption"""
import commands


def startPrompt():
    # mmm
    c = commands.command("prompt")

    crash = False
    print "please type help to see all the commands"
    while crash is not True:
        cinput = str(raw_input(">"))
        if cinput == "":
            print "Remember to write something before hitting ENTER."
            continue
        elif cinput == "quit":
            c.quit()
            crash = True
            # bye bye
        elif cinput == "help":
            c.help()

        elif cinput == "encrypt":
            c.encrypt()

        elif cinput == "license":
            c.license()
