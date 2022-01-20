#WAP to check weather given number is perfect number or not
number=int(input("Enter a number to check weather it is perfector not"))
sum1=0
for i in range(1,number):
    if number%i==0:
      sum1=sum1+i
if sum1==number:
    print("entered number is perfect")
        
else:
    print("entered number is not perfect")
        
    