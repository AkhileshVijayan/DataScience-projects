#Anyone can use these functions to create email or password validation
import re #This is a python package or library for regular expression

def username():
 regex = '^(([a-zA-z]+)|([a-zA-z][0-9]+))+@[a-zA-Z]+\.[A-Za-z]{2,5}$' #We can make our own regular expression
 Username =  input("Create a username:")
 if re.search(regex,Username):
     print("Valid")
 else:
     print("Invalid")
     username()

def password_requirement():
    print("""
              CHARACTERISTICS OF STRONG PASSWORDS
          .............................................    
          1.Length of password should between 5 and 16.
          2.Atleast one uppercase and lowercase letters.
          3.Atleast one letter and number.
          4.Inclusion of at least one special character, e.g., ! @ # ? ] % &

              """)
def password():
    password1 = input('Create a password:')
    if (len(password1)<5):#We can change the length as per our requirement
        print("Password is too short.")
        print("Re-enter the password")
        password()
    elif (len(password1)>16):
        print("Password is too long")
        print("Re-enter the password")
        password()
    elif (5<len(password1)<16):
     regex1 = '^(?=.{5,16}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$'
     if(re.search(regex1,password1)):
           print("Valid")
     else:
           print("Invalid")
           password()

username()
password_requirement()
password()