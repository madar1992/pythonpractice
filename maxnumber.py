#WAP to accept 3 numbers and find max number.
number1=int(input("Enter number1 "));
number2=int(input("Enter number2 "));
number3=int(input("Enter number3 `  "));

if number1>number2 and number1>number3:
    print("number 1 is max")
elif number2>number1 and number2>number3:
    print("number 2 is max")
else:
    print("number 3 is max")
    
    