from Student import Student
from Presentation import Presentation

Presentation.make_presenations_from_csv("/Users/carterkelly/Desktop/CS Python/Capstone/April Capstone Sessions.csv")
Student.make_students_from_csv("/Users/carterkelly/Desktop/CS Python/Capstone/Capstone Requests No Names.csv")

sub_students = [student for student in Student.all_students if student.request[0] != "any"]
any_students = [student for student in Student.all_students if student.request[0] == "any"]

print("REPORT:")

for student in Student.all_students:
    student.assign_student()
    student.assign_rnd_presentation()
    print(student)

# print("STUDENTS WITH FORM")
# for sstudent in sub_students:
#     sstudent.assign_student()
#     print(sstudent)

# print("STUDENTS WITHOUT FORM")
# for astudent in sub_students:
#     astudent.assign_rnd_presentation_other()
#     print(astudent)

for pres in Presentation.all_presentations.values():
    print(pres)


print("SINNERS:")
for student in Student.all_students:
    if student.schedule["1"] == student.schedule["2"] or student.schedule["2"] == student.schedule["3"] or student.schedule["1"] == student.schedule["3"]:
        print(f"{student.name} has DUPLICATE")

for student in Student.all_students:
    if None in student.schedule.values():
        print(f"{student.name} has a None")




# Student.all_students[300].assign_student()
# Student.all_students[212].assign_rnd_presentation()