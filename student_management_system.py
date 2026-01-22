# Student Result Management System (SRMS)

student_results = {}

def add_student_result(name, score):
    student_results[name] = score

def display_results():
    for name, score in student_results.items():
        print(f"Student Name: {name}, Score: {score}")

# Main Program
add_student_result("John", 75)
add_student_result("Mary", 88)

display_results()
