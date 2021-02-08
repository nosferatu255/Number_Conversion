###################### Number Conversion $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
######## By nosferatu255 $$$$$$$$$$$$$$$$

#Funkcija za dec u bin
def dec_bin(x):
    if x >= 1:
        dec_bin(x // 2)
    print(x % 2, end='')

 #Funkcija za dec u hex
def dec_hex(x):
    c = hex(x)
    print("0x means that the value is in Hexadecimal.\n" + c)
     #Funkcija za dec u oct
def dec_oct(x):
   c = oct(x)
   print("0o means that the value is in Octal.\n" + c)

# Funkcija za bin u dec
def bin_dec(x):
    dec = 0
    p = 0
    while x>0:
        dec += 2 **p* (x%10)
        x //=10
        p += 1
        print(dec)

        #Za hex u dec
def hex_dec(x):
    c = int(x,16)
    print(str(c))

#Za oct u dec
def oct_dec(x):
    c = int(x,8)
    print(str(c))

base = str(input("Enter a number of the conversion\n" + 
                 "1-Decimal to Binary\n2-Decimal to Hexadecimal\n3-Decimal to Octal\n" + 
                 "4-Binary to Decimal\n5-Hexadecimal to Decimal\n6-Octal to Decimal\n"))

if base == "1":
    number = int(input("Enter a number\n"))
    dec_bin(number)
    
elif base == "2":
    number = int(input("Enter a number\n"))
    dec_hex(number)

elif base == "3":
    number = int(input("Enter a number\n"))
    dec_oct(number)

elif base == "4":
    number = int(input("Enter a binary number\n"))
    bin_dec(number)

elif base == "5":
    number = input("Enter a hexadecimal number\n")
    hex_dec(number)

elif base == "6":
    number = input("Enter a octal number\n")
    oct_dec(number)
