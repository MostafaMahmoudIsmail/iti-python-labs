while True:
    n = input("Enter The radius of the circle : ")
    if n.isalpha():
        print("Not Valid Num")
        continue
    else :
        break
radius = int(n)
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius
print("Area of the circle:", round(area,2))
print("Circumference of the circle:", round(circumference,2))