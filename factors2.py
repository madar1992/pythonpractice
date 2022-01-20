#WAP to find no.of factors for given number.
number=int(input("enter number to know no.of factors"))
x=0
for i in range(1, number+1):
    if number%i==0:
      x+=1
print(x)
   
    
      