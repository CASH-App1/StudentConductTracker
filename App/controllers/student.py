from App.models import Student
from App.database import db 

# Controller to add a new student
def add_student(studentID, first_name, last_name):
    new_student = Student(studentID=studentID, fname=first_name, lname=last_name)
    db.session.add(new_student)
    db.session.commit()
    return new_student

# Controller to get a student by username (student_id)
def get_student(studentID):
    return Student.query.get(studentID)

# Controller to get a list of all students
def get_all_students():
    students = Student.query.all()
    student_data = [{'studentID': student.studentID, 'firstName': student.firstName, 'lastName': student.lastName} for student in students]
    return student_data

# Controller to get a list of students with a specific first name and last name
def get_students_by_name(first_name, last_name):
    students = Student.query.filter_by(fname=first_name, lname=last_name).all()
    
    # Create a list of dictionaries containing student data
    student_search = [{'studentID': student.studentID, 'firstName': student.fname, 'lastName': student.lname} for student in students]
    return student_search
    
# Controller to update a student
def update_student(studentID, new_first_name, new_last_name):
    student = Student.query.get(studentID)
    if student:
        student.fname = new_first_name
        student.lname = new_last_name
        db.session.add(student)
        db.session.commit()
        return student
    return None

