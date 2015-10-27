
from random import randint

secretNr = randint(1,100)


guess = -1

while(guess != secretNr):
    guess = input("Gaet et tal mellem 1 og 100: ")
    if(guess < secretNr):
        print "Det er for lavt du!"
    elif(guess > secretNr):
        print "Det er for hoejt du!"
    else:
        print "Du ramte rigtigt"
