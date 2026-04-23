import re
password = r"^[\w@#$%^&*_\-!~><\./?]{8,}$"
strong_password = r"^(?=.*[@#$%^&*_\-!~><\./?])(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
a = input("Enter the password: ")
if re.fullmatch(password, a):
    print("Valid Password")
    if re.fullmatch(strong_password, a):
        print("Strong Password")
else:
    print("Invalid Password")