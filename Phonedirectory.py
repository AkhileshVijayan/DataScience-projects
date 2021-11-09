a= []
for i in range(7):
    id = int(input("id:"))
    n = input("Name:")
    m = (input("whatsapp number or not:").lower())
    if m =='yes':
        mobile = int(input("Enter your whatsapp number"))
    else:
        print("Entry is only for whatsapp number.Please create and submit later")
    email = input("Please type 'yes'if email domain ends with gmail.com") .lower()
    if email == 'yes':
     e = input("Enter your email id:")
     while True:
      if("@gmail.com" in e):
         print("Email id is valid")
         break
      else:

          e = input("Enter your gmail id correctly")

    else:
          print("please create a gmail account and submit later")
          continue
    a.append({"_id":id,"Name":n,"Mobile":mobile,"Emailid":e})
print(a)
b.insert_many(a)










