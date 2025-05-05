emoticon=" ^^"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon=":D"
    say("oh, hi")

def say(phrase):
    print(phrase+ " "+ emoticon)


main()       