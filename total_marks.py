#WAP to accept project marks,internal marks,external marks and find total marks.
#total_marks=70% from project+20% from extenal+10% from internal.

project_marks=int(input("Enter your project_marks= "));
external_marks=int(input("Enter your external_marks= "));
internal_marks=int(input("Enter your internal_marks= "));

total_marks=(70*project_marks/100)+(20*external_marks/100)+(10*internal_marks/100);
print("the total marks are= ",total_marks);

