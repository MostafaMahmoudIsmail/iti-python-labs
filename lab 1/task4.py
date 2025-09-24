n = input("Enter The radius of the circle : ")
if n.isalpha():
    print("Not Valid Num")
    exit()
radius = int(n)
area = 3.14 * radius ** 2
circumference = 2 * 3.14159 * radius
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)