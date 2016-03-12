"""crypt.py in Pycryption"""


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
            break


