#wap to accept 3 subjects marks and print total marks and avg marks.

sub1=int(input("Enter sub1 marks"));
sub2=int(input("Enter sub2 marks"));
sub3=int(input("Enter sub3 marks"));

total=sub1+sub2+sub3;
avg=total//3;
print("Total of 3 subjects is= ",total);
print("Average of 3 subjects is= ",avg);