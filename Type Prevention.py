#-------------Pervent the user form entering the wrong type----------#
#--------6-------------6----------------6---------#
#----------B-Y--N-O-S-F-E-R-A-T-U------------------#
while(1):
    try:
        inp = int(input("Enter a Number\n"))
        if type(inp) == int:
            break
    except ValueError:
        print("Bad input!")
print("Nois")    

# Just a code that prevents the code from breaking if the user
# inputs the wrong type for a variable

# Explanation :

# while(1) <- this is an infinite loop so that the code runs until you want

# try:
#    inp = int(input("Enter a Number\n"))
#    if type(inp) == int:
#        break                 <- if you enter a number the program will
#                                 just continue but if you enter something else
#                                 like a letter it will jump to the except block


# except ValueError:
#        print("Bad input!")  <- every time the inp is not an int this will run
#print("Nois")                  but because the loop is infinite it will run
#                               until the input is right

