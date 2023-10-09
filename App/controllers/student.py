from App.models import Student
from App.database import db

# Controller to add a new student
def add_student(studentID, first_name, last_name):
    new_student = Student(studentID=studentID, firstName=first_name, lastName=last_name)
    db.session.add(new_student)
    db.session.commit()
    return new_student

# Controller to get a student by username (student_id)
def get_student(studentID):
    return Student.query.filter_by(studentID=student_id).first()

# Controller to get a list of all students
def get_all_students():
    students = Student.query.all()
    student_data = [{'studentID': student.studentID, 'firstName': student.firstName, 'lastName': student.lastName} for student in students]
    return student_data

# Controller to update a student
def update_student(studentID, new_first_name, new_last_name):
    student = Student.query.filter_by(studentID=studentID).first()
    if student:
        student.firstName = new_first_name
        student.lastName = new_last_name
        db.session.add(student)
        db.session.commit()
        return student
    return None

