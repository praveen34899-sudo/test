num=[20,45,35,60,10,53,23,48,40]
even=filter(lambda no:no%2|0,num)
print(list(even))
salarys=(20000,30000,40000,50000,60000)
hike=map(lambda salary:salary*0.10+salary,salarys)
print(list(hike))
fname=['anu','raj','mary']
lname=['priya','kumar','james']
fullname=map(lambda n1,n2:n1+" "+n2,fname,lname)
print(list(fullname))
from functools import reduce
sales_by_week=[23000,30000,28000,32000,25000]
total_sales=reduce(lambda x,y:x+y,sales_by_week)
print(total_sales)