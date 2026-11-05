user_name="praveen" 
password="praveen@123"
while True:
    user_name=input("enter the user name:")
    password=input("enter the password:")
    if user_name==user_name and password==password:
        print("login succesfully")
        break
    else:
        print("try again")