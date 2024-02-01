import string
import random
print("                   PASSWORD GENERATOR                    ")
length=int(input("ENTER THE PASSWORD LENGTH:"))
letter=string.ascii_letters
no=string.digits
characters=string.punctuation
tot=letter+no+characters

temp= random.sample(tot, length)
password="".join(temp)
print("HERE'S YOUR NEW PASSWORD",password)

