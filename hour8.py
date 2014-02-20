while True:
    name = raw_input("Please, give me a name: ")
    if name == "q":
        break
    def find_name(name):
        name_list = ["kalle", "niklas", "petter"]
        if name in name_list:
            print "That student is IN the list!"
            return True
        else:
            print "That student is NOT in the list"
            return False
        
    print find_name(name)
