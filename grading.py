    # WAP to accept project marks, external marks, internal marks from student,
      #  --> check if student got pass in project, internal and externals. 
        #  Note: pass mark is : 50
      #--> if student got pass in project, internal and external then find totalscore.
       # total_score= 70% from project+ 20% from external + 10% internal 

  #   --> print grades based on total_score
   #         
     #      total_score >=90    --> A grade
    #		              75--90      --> B grade
  #               50- 75      --> C grade
     #
   #  ---> print failed subject name along with the score.
project_marks=int(input("Enter your project_marks= "))
External_marks=int(input("Enter your external marks= "))
Internal_marks=int(input("Enter your internal marks= "))

total_score=(70*project_marks/100)+(20*External_marks/100)+(10*Internal_marks/100)

if project_marks and External_marks and Internal_marks>=50:
      print("you are passed and your total marks are= ",total_score)
if total_score>=90:
 print("your grade is A ")
if total_score>75:
 print("your grade is B ")
if total_score>50:
 print("your grade =is C ")

if project_marks<50:
 print("you are failed in project work ",project_marks)
if External_marks<50:
 print("you are failed in Externals ",External_marks)
if Internal_marks<50:
 print("you are failed in Internals ",Internal_marks) 
 


 