courses={"ai","python","c","c++","java","mangodb"}
count=0
for new in courses:
    count=count+1
    print(f"{count}.{new}")
tuple(courses)
i=0
for value in courses:
    i=i+1
    print(f"{i}.{value}")
employee={'empid':555,'empname':'ram','salary':500000,'des':"ai"}
j=0
for key in employee:
    j=j+1
    print(f"{j}.{key}:{employee}")

