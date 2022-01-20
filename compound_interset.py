#WAP to find compound interset.
principal = float(input("Enter amount: "))
time = float(input("Enter time: "))
rate = float(input("Enter rate: "))


compound_interest = principal *((1+rate/100)**time - 1)

print("Compound interest is: ",(compound_interest))