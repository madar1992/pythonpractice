#WAP to accept and 3 shopping billsfrom user and find
#1. total shopping amount
#2.find how much % of amount he/shetotal shopping amount

salary=float(input("Enter your salary"));
shopping_bill_1=float(input("Enter your shopping bill 1 "));
shopping_bill_2=float(input("Enter your shopping bill 2 "));
shopping_bill_3=float(input("Enter your shopping bill 3 "));

total_shopping_amount=shopping_bill_1+shopping_bill_2+shopping_bill_3;
percentage=(total_shopping_amount/salary)*100;

print("total shopping amount is= ",total_shopping_amount);
print("percentage of salary spent on shopping is= ",percentage);