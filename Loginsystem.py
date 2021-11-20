import re

def access(option):

    if(option == "1"):
      username()
      password_menu()
      password1()
      register(Username,password)
    else:
       username()
       password1()
       login(Username,password)

def begin():
    global option
    print("Welcome to GUVI online login system", "\n")
    print("Kindly select an option")
    print(" 1. Registration")
    print(" 2. Login")
    option = input("Make your entry here:")
    if (option != "1" and option != "2"):
        print("Please enter a valid option")
        print("Thank you")
        print("\n")
        begin()

def forget_password():
    Username = input("Kindly enter your username:")
    file = open("Logindb.txt", 'r')
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == Username):
            print("Hi," + Username + " your password is:" + b)
    file.close()

def login(Username,password):
 success = False
 file = open("Logindb.txt",'r')
 for i in file:
     a,b = i.split(",")
     b = b.strip()
     if(a==Username and b == password):
         success = True
         break
 file.close()
 if(success):
     print("Hi," + Username+"\n"+ " Login successful!!!")


 else:
     failure = False
     file = open("Logindb.txt", 'r')
     for i in file:
         a, b = i.split(",")
         b = b.strip()
         if(a==Username):
             failure =True
             break
     file.close()
     if(failure):
         print("""Did you forget your password!!...
                    Don't worry!!!
                    You can retrieve the old password within seconds!!
         """)
         forget_password()
         print("\n")
         print("Please try to login again!!!")
         print("\n")
         begin()
         access(option)
     else:
       print("Username doesn't exist")
       print("Please register")
       print("""
             THANK YOU:)
             -----------
       """)
       begin()
       access(option)




def register(Username,password):
 success = False
 file = open("Logindb.txt",'r')
 for i in file:
        c, d = i.split(",")
        d = d.strip()
        if(c==Username):
          success = True
          break
 file.close()
 if(success):
     print("Username already exists")
     print("You are already registered. Please try to login")
     print("""
             THANK YOU:)
             -----------         
     """)
     print("\n")
     begin()
     access(option)
 else:
         file = open("Logindb.txt", 'a')
         file.write("\n"+Username + "," + password)
         print("Registered successfully")

 file.close()




def username():
 global Username
 regex = '^(([a-zA-z]+)|([a-zA-z][0-9]+))+@[a-zA-Z]+\.[A-Za-z]{2,5}$'
 Username =  input("Enter username:")
 if re.search(regex,Username):
     return(Username)

 else:
     print("The username that you have entered is not valid")
     username()

def password_menu():
    print("""
               CHARACTERISTICS OF STRONG PASSWORDS
           .............................................    
           1.Length of password should between 5 and 16.
           2.Atleast one uppercase and lowercase letters.
           3.Atleast one letter and number.
           4.Inclusion of at least one special character, e.g., ! @ # ? ] % &

               """)
def password1():
    global password

    password = input('Enter the password:')
    if (len(password)<5):
        print("Password is too short.")
        print("Re-enter the password")
        password1()
    elif (len(password)>16):
        print("Password is too long")
        print("Re-enter the password")
        password1()
    elif (5<len(password)<16):
     regex1 = '^(?=.{5,16}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$'
     if(re.search(regex1,password)):
           return(password)
     else:
           print("Password doesn't meet the requirements"+"."+" Please try again")
           password1()



begin()
access(option)
