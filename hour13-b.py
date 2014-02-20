from random import randint

number = randint(1, 10)

while True:
    guess = raw_input("Guess number 1 - 10: ")
    if int(guess) > number:
        print "To high !"
    elif int(guess) < number:
        print "To low !"
    else:
        print "You guessed the right number: " "{}".format(number)
        break
    
    
