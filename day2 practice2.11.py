#WAP to print prime numbers i-n in the given range and input should be taken by user.

lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: ")) 
count=0
print ("The Prime Numbers in the range are: ")  
for x in range (lower_value, upper_value + 1):  
    if x > 1:  
        for i in range (2, x//2):  
            if (x % i) == 0:
                count=count+i
    else:
        print ("entered lower_value is invaild")  
