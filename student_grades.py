#disctionary for student scores 
student_scores = {
"Harry" : 81, 
"Ron" : 78, 
"Hermione" : 99, 
"Draco" : 74, 
"Neville" : 62,
}

#grades and values
#91-100 : "Outstanding",
#81-90 : "Exceeds Expectations", 
#71-80 : "Acceptable",
#70 or below : "Fail",   

#dictionary to store grades for students
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] =  "Outstanding"
    elif (score <= 91) and (score >= 81):
        student_grades[student] = "Exceeds Expectations"
    elif (score <= 81) and (score >= 71):
        student_grades[student] = "Acceptable"  
    elif (score <= 70):
        student_grades[student] = "Fail"

#print out the student and their grade
print(student_grades)
