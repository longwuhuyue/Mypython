import time
shipname = "Nastrama"
captain = "Wallace"
location = "Earth"
password = "asd,./123"
pattempt = raw_input("Enter the password: ")
while pattempt != password:
    print   "Password incorrect"
    pattempt = raw_input("Enter the password: ")
print "Password correct.Welcome to the " +shipname
print ""
print "The spaceship " + shipname  + " is currently visiting " + location + "."
choice = ""
while choice != "q":
    print "What would you  like to do, " +captain + "?"
    print " a: Travel to another planet \n b: Fire cannons \n c: open the airlock \n d: Self-destruct \n q to exit"
    print ""
    choice = raw_input("Enter your choice: ")
    if choice == "a":
        destination = raw_input("Where would you like to go? ")
        print   "leaving:" + location
        print "Travelling to " + destination
        time.sleep  (5)
        location = destination
    elif  choice =="b":
        print "Firing cannons"
        time.sleep (1)
        print "BANG!"
        time.sleep(1)
    elif choice =="c":
        print "Opening airlock"
        time.sleep(3)
        print"Airlock open"
        time.sleep(1)
    elif choice == "d":
        confirm = raw_input("Are you sure you want the ship to self-destruce?(y/n)")
        if confirm == "y":
            print "Ship will self-destruct in"
            print "3"
            time.sleep(1)
            print "2"
            time.sleep(1)
            print "1"
            time.sleep(1)
            print "Good bye!"
            time.sleep(1)
            print "BOOM!"
            choice = "q"
    elif choice =="q":
        print " GoodBye!"
    else:
        print "Invalid input. Please select a,b,c,d or d.q to exit."
            
        
        
        
    
