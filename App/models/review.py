from App.database import db

class Review(db.Model):
  reviewID: db.Column(db.String(5), primary_Key=True)
  studentID: db.Column(db.String(5),  db.ForeignKey('student.studentID'))
  staffID: db.Column(db.String(5), nullable=False)
  description: db.Column(db.String(1000), nullable=False)
  date: db.Column(db.DateTime, default = datetime.utcnow)
  upvote: db.Column(db.Integer, nullable=False)
  downvote: db.Colum(db.Integer, nullable=False)
  type: db.Column(db.String(8), nullable=False)

  def __init__(self, studentID, staffID, description):
    self.studentID = studentID
    self.staffID = staffID
    self.description = description


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

  def upvoteReview(self):
        #for review in reviews:
         #   if reviewID == review.reviewID:
          #      if review.student.karmaScore != 10
           #         review.student.karmaScore += 1
    self.upvote += 1

  def downvoteReview(self):
        #for review in reviews:
         #   if reviewID == review.reviewID:
          #      if review.student.karmaScore != 0
           #         review.student.karmaScore -= 1
    self.downvote += 1

