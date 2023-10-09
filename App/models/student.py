from App.database import db

class Student(db.Model):
  studentID: db.Column(db.String(5), nullable=False)
  fname: db.Column(db.String(30), nullable=False)
  
