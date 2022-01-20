#WAP to accept basic salary and find gross salary.
#Gross_salary=basic+HRA+DA
#if basic_salary <10000
#      DA is 70% on basic
 #     HRA is 65% on basic
#    basic salary is between 10000 to 20000
#       DA is 75% on basic
#       HRA is 73% on basic
#    basic salary above 20000
#     DA is 80% on basic
#      HRA is 76% on basic

basic_salary=float(input("Enter your basic_salary "));
if basic_salary<10000:
  DA=70*basic_salary/100;
  HRA=65*basic_salary/100;
  
elif basic_salary>10000 and basic_salary<20000:
      DA=75*basic_salary/100;
      HRA=73*basic_salary/100;
      
else:
      DA=80*basic_salary/100;
      HRA=76*basic_salary/100;
     
Gross_salary=basic_salary+HRA+DA
      
print("The gross salary is= ",Gross_salary)
  
     



