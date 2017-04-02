students = {}

students = {"Alice": 25, "Bob": 31, "Rob": 28}

print(students["Alice"])

students["Claire"] = 18

print(students)

students["Alice"] = 26

print(students["Alice"])

del students["Claire"]

print(students)

print(students.keys())

student_names = list(students.keys())

student_ages = list(students.values())

print("Student names {} student ages {}".format(student_names, student_ages))