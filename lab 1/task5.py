name = input("Enter Your Name : ")
if not name or name.isdigit():
    print("not valid Name")
    exit()

email = input("Enter Your Email : ")
if not email or "@" not in email:
    print("not valid Email")
    exit()

print(f"Your Name Is {name} And Your Email Is {email}")
