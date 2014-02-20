value = 0.0
total = 0.0

while True:
    value = raw_input("Enter the value for the seat: ")
    if value == "q":
        break
    if value.isdigit() == False:
        value = 0
        print "Not an accepted value"
    total = total + float(value)
print "**********"
print "Total: {}".format(total)
    
 
