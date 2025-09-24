while True:
    n = input("Enter Your Binary Number : ")
    if n.isalpha():
        print("invalid Binary Number")
        continue
    else :
        break

print("The Decimal Representation is : ",int(n,2))
