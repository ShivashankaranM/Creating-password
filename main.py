import random as rnd
Characters="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
Passcode=int(input("Enter the number of the password characters required"))
Password="".join(rnd.sample(Characters,Passcode))
print(Password)
