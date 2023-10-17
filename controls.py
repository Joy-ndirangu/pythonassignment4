# mini grading system
# maths, physics, geo, chem
maths = int(input("enter student's maths marks"))
physics = int(input("enter student's physics marks"))
geo = int(input("enter student's geography marks"))
chem = int(input("enter student's chemistry marks"))
if(maths>0 or maths>100) or (physics>0 or physics>100) or (geo<0 or geo>100) or (chem<0 or chem>0):
    print("unrecognized marks entered")


marks = (maths + physics + geo + chem) / 4
print(marks)
if marks > 70 and marks < 100:
    grade = 'A'
    print("The grade is: ", grade)
elif marks > 50 and marks < 71:
    grade = 'B'
    print("The grade is: ", grade)
elif marks > 40 and marks < 51:
    grade = 'C'
    print("The grade is: ", grade)
else:
    grade = 'D'
    print("The grade is : ", grade)