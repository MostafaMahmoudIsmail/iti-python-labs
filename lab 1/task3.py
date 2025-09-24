def check(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "buzz" 
    else :
        return "invalid Number"


while True:
    n = input("Enter The Number : ")
    if n.isalpha() or not n.isdigit():
        print("Invalid Number")
        continue
    else :
        n = int(n)
        print(check(n))


