students = {}

while True:
    name = raw_input("Name: ")
    grade = raw_input("Grade: ")
    students[name] = grade
    if name == "q":
        print students
        break
        
    
