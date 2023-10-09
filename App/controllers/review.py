
from App.model import *

#Controller of staff to log review for student
def log_review(studentID, review, type):
    newReview = Review(studentID=studentID, review=review, type=type)
    db.session.add(newReview)
    db.session.commit()

#Retrieving reviews done by staff
def get_all_reviews():
    return Review.query.all()

#Upvote review
def upvote_review(reviewID):
    review = Review.query.get(reviewID)
    if review:
        upvote = review.upvoteReview(reviewID)
        db.session.add(upvote)
        db.session.commit()
        return True
    return False

#Downvote review
def downVote_review(reviewID):
    review = Review.query.get(reviewID)
    if review:
        downvote = review.downvoteReview(reviewID)
        db.session.add(downvote)
        db.session.commit()
        return True
    return False

#Controller to get a review by reviewID
def get_review(reviewID):
    return Review.query.filter_by(reviewID=reviewID).first()
