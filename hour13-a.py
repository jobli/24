from random import random

tested = 0

while True:
    number = random()
    test_number = raw_input("Test random number? [y/n] ")
    if test_number == "y":
        print number
        tested = tested + 1
        print tested
    if test_number == "n":
        print "Total times of testing = " "{}".format(tested)
        break
    
    
                        
