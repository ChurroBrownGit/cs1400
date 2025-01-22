#Goal 1
def myname():
    print("Joel")

myname()

#Goal 2
def lovebirds(name1, name2):
    print(str(name1) + " loves " + str(name2) + ".")

name1 = input("What is the first name?")
name2 = input("What is the second name?")
lovebirds(name1,name2)

#Goal 3
print("'''"''""''"")
#This will give SyntaxErrors.

#Challenge 1
def password_check(password1,password2):
    if str(password1) == str(password2):
        return True
    else:
        return False
    
password1 = input("What is the first password?")
password2 = input("What is the second password2?")
passwordmatch = password_check(password1,password2)
print(str(passwordmatch))