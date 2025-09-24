n = input("Enter Your Binary Number : ")
if n.isalpha():
    print("invalid Binary Number")
    exit()
print("The Decimal Representation is : ",int(n,2))
