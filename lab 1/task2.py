nums = ['2','3','4','5','6','7','8','9']
while True:
    n = input("Enter Your Binary Number : ")
    flag = 0
    if n.isalpha():
        print("invalid Binary Number")
        continue
    else :
        for i in nums:
            if n.count(i):
                flag = 1
                break
                
    if flag:
        print("invalid Binary Number")
        continue
    else :
        break


print("The Decimal Representation is : ",int(n,2))
