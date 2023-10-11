from App.database import db
from datetime import datetime

class Review(db.Model):
  reviewID: db.Column(db.Integer, primary_key=True)
  studentID: db.Column(db.Integer,  db.ForeignKey('student.studentID'))
  staffID: db.Column(db.String(5), nullable=False)
  description: db.Column(db.String(1000), nullable=False)
  date: db.Column(db.DateTime, default = datetime.utcnow)
  upvote: db.Column(db.Integer, nullable=False)
  downvote: db.Column(db.Integer, nullable=False)
  reviewType: db.Column(db.String(8), nullable=False)

  def __init__(self, studentID, staffID, description, reviewType):
    self.studentID = studentID
    self.staffID = staffID
    self.description = description
    self.reviewType = reviewType


  def toDict(self):
    return{
      'Review ID': self.reviewID,
      'Student ID': self.studentID,
      'Staff ID': self.staffID,
      'Description' : self.description,
      'Date' : self.created.strftime("%Y/%m/%d, %H:%M: %S"),
      'Upvote': self.upvote,
      'Downvote': self.downvote,
      'Review Type' : self.type
    }

  def upvoteReview(self):
    self.upvote += 1

  def downvoteReview(self):
    self.downvote += 1

