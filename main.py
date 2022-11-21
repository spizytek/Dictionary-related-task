student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
grade_bo= 0
for grade in student_scores:
    
    grade_bo = student_scores[grade]
     #Scores 91 - 100: Grade = "Outstanding"  
    if( (grade_bo <= 100) and (grade_bo >= 91)):
        student_grades[grade] = "Outstanding"
     #Scores 81 - 90: Grade = "Exceeds Expectations"
    elif(  (grade_bo <= 90) and (grade_bo >= 81) ):
        student_grades[grade] = "Exceeds Expectations"
    #Scores 71 - 80: Grade = "Acceptable"
    elif(  (grade_bo <= 71) and (grade_bo >= 80) ):
        student_grades[grade] = "Acceptable"
    #Scores 70 or lower: Grade = "Fail"
    elif(  (grade_bo <= 70) ):
         student_grades[grade] = "Acceptable"


# 🚨 Don't change the code below 👇
print(student_grades)





