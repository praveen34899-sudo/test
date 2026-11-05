name=input("Enter your name:").upper()
age=int(input("Enetr your age:"))
gender=input("Enter you gender:").lower()
marriage_status=input("Enter your Marriage status:").lower()
if(marriage_status=="yes")and(age>30)and(gender=="male"):
    print(f"NAME={name}\nAGE={age}\nINSURANCE_AMOUNT=₹10000".upper())
elif(marriage_status=="yes")and(age>27)and(gender=="female"):
    print(f"NAME={name}\nAGE={age}\nINSURANCE_AMOUNT=₹12000".upper())
elif(marriage_status=="no")and(age>35)and(gender=="male"):
    print(f"NAME={name}\nAGE={age}\nINSURANCE_AMOUNT=₹5000".upper())
elif(marriage_status=="no")and(age>30)and(gender=="female"):
    print(f"NAME={name}\nAGE={age}\nINSURANCE_AMOUNT=₹7000".upper())
else:
    print("NOT ELIGIBLE")