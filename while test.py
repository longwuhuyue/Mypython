username = raw_input("What's your name: ")
message = raw_input ("Enter a massage: ")
while message != "exit":   # can't use if nore it will not be circal
    print username + ": " + message
    message = raw_input("Enter a mas: ") 
