toppings = ["pepperoni", "sausage", "cheese", "peppers"]
choosen_toppings = []
choice_1 = raw_input("Please, give me a topping: ")
choice_2 = raw_input("Please give me one more topping: ")
if choice_1 in toppings:
    choosen_toppings.append(choice_1)
else:
    print "Sorry, we do not have {}".format(choice_1)
if choice_2 in toppings:
    choosen_toppings.append(choice_2)
else:
    print "Sorry, we do not have {}".format(choice_2)

print "Here are your toppings:"
print choosen_toppings
    
