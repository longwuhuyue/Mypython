ask = raw_input("Do you want a praise:")
if ask =="yes":
    again = "yes"
    while again == "yes":
        praisetype = raw_input("Select a type of praise \n a: personality \n b: apperarance \n c: intelligence \n :")
        if praisetype == "a":
            print "You are an insteresting person"
        elif praisetype == "b":
            print "You are smart"
        elif praisetype == "c":
            print "You look good"
        else:
            print "That wasn't an option"
        again = raw_input("Would you like some more praise?")
