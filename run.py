"""

def madlibs04():


    print("Nursery Rhymes.")

    adjective41 = input("An adjective:\n")
    advedrb41 = input("An adverb:\n")
    adjective42 = input("Another adjective:\n")
    bodypart41 = input("Body part plural:\n")
    bodypart42 = input("Another body part plural:\n")
    

    if adjective41.isalpha() is False:
        print("Please make sure you type words only.")
        madlibs04()
    elif advedrb41.isalpha() is False:
        print("Please make sure you type words only.")
        madlibs04()
    elif adjective42.isalpha() is False:
        print("Please make sure you type words only.")
        madlibs04()
    elif bodypart41.isalpha() is False:
        print("Please make sure you type words only.")
        madlibs04()
    elif bodypart42.isalpha() is False:
        print("Please make sure you type words only.")
        madlibs04()
    else:
        madlibs3 = print(
            f"When some {adjective41} " +
            f"school students were asked what nursery " +
            f"rhymes popped {advedrb41} " +
            f"into their {adjective42} " +
            f"or were on the tip of their {bodypart41}" +
            f", these were their {bodypart42} answers:")




def main():
    madlibs04()


main()

"""

string = input("Enter a word: ")
toldo = input("Enter a a thing: ")
goldo = input("Enter a stuff: ")


if not all(x.isalpha() or x.isspace() for x in string):
    print("Only alphabetical letters and spaces: nooooo")
elif not all(x.isalpha() or x.isspace() for x in toldo):
    print("Only alphabetical letters and spaces: nooooo")
elif not all(x.isalpha() or x.isspace() for x in goldo):
    print("Only alphabetical letters and spaces: nooooo")
else:
    print("YEESSS")