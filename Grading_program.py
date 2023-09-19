student_scores={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}
student_grades={}
for student in student_scores:
    scores=student_scores[student]
    if scores>91 and scores<100:
        student_grades[student]="outstanding"
    elif scores>81:
        student_grades[student]="Exceeds Expectations"
    elif scores>71:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="fail"
print(student_grades)



    
    
       
    