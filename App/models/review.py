from App.database import db

class Review(db.Model):
  reviewID: db.Column(db.String(5), primary_Key=True)
  studentID: db.Column(db.String(5),  db.ForeignKey('student.studentID'))
  staffID: db.Column(db.String(5), nullable=False)
  description: db.Column(db.String(1000), nullable=False)
  date: db.Column(db.DateTime, default = datetime.utcnow)
  upvote: db.Column(db.Integer, nullable=False)
  downvote: db.Coulum(db.Integer, nullable=False)

  def __init__(self, reviewID, studentID, staffID, description, upvote, downvote):
    self.reviewID = reviewID
    self.studentID = studentID
    self.staffID = staffID
    self.description = description
    self.upvote = upvote
    self.downvote = downvote

    
  def toDict(self):
    return{
      'Review ID': self.reviewID,
      'Student ID': self.studentID,
      'Staff ID': self.staffID
      'Description' : self.description
      'Date' : self.created.strftime("%Y/%m/%d, %H:%M: %S")
      'Upvote': self.upvote
      'Downvote'= self.downvote
    }
      

  

