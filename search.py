#WAP to count number of occurance of search element.
count=0
list=[23,45,56,23,23,90,77]
num=int(input("enter number"))
for i in list:
    if num==i:
        count=count+1
if count!=0:
    print(count)
else:
    print("no")