name=str(input("Enter the name of the student :"))
print("ENTER THE MARK")
T=int(input("TAMIL :"))
E=int(input("ENGLISH :"))
M=int(input("MATHS :"))
S=int(input("SCIENCE :"))
SS=int(input("SOCIAL SCIENCE :"))
print("NAME :",name)
print("TAMIL :",T)
print("ENGLISH :",E)
print("MATHS :",M)
print("SCIENCE :",S)
print("SOCIAL SCIENCE :",SS)
TOTAL_MARKS=T+E+M+S+SS
print("TOTAL =",TOTAL_MARKS)
TOTAL_AVERAGE=TOTAL_MARKS/500*100
print("AVERAGE =",TOTAL_AVERAGE)
if TOTAL_AVERAGE>=40:
    print("PASS")
else:
    print("FAIL")
