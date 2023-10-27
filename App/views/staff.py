from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user, get_jwt_identity
from flask_login import current_user, login_required

from App.controllers import *

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/post', methods=['POST'])
@jwt_required()
def logReview():
    data = request.json
    username = get_jwt_identity()
    # staff = StaffMember.query.get(username)
    # print("before if staff")
    # print(staff.username)
    
    #if staff:
    if data["type"] not in ["positive", "negative"]:
        return jsonify(error = "Invalid review type"), 400
    student = Student.query.get(data['studentID'])
    if not student:
        return jsonify(error = 'Student not found'),400
    review = log_review(username,  data['studentID'],data['review'], data['type'])
    if review:
        return jsonify(message = 'Review logged successfully'), 201
    return jsonify(error='Review failed to post'), 400


@user_views.route('/view/student', methods=['GET'])
@jwt_required()
def view_student():
    data = request.json
    student = get_student(data['studentID'])
    if student:
        return jsonify(student.toDict()), 200
    return jsonify(error='Student not found'), 400

@user_views.route('/view/student/review', methods=['GET'])
@jwt_required()
def view_review():
    data = request.json
    student = get_student(data['studentID'])
    if student:
        review = get_review(data['reviewID'])
        if review:
            return jsonify(review.toDict()), 200
        return jsonify(error='Review not found'), 400
    return jsonify(error='Student not found'), 400


@user_views.route('/add-student', methods=['POST'])
@jwt_required()
def add_Student():
    data = request.json
    student = Student.query.get(data['studentID'])
    if student:
        return jsonify(error='A student already exists with this ID'), 400
    student = add_student(data['studentID'], data['firstName'], data['lastName'])
    if student:
        return jsonify(message='Student added successfully'), 200
    return jsonify(error='Student could not be created'), 500

@user_views.route('/update-student', methods=['PUT'])
@jwt_required()
def update_Student():
    data = request.json
    student = update_student(data['studentID'], data['firstName'], data['lastName'])
    if student:
        return jsonify(message='Student updated successfully'), 200
    return jsonify(error='Update unsuccessful'), 400


@user_views.route('/search', methods=['GET'])
@jwt_required()
def search_student():
    print("here")
    data = request.json
    print(data)
    student = get_students_by_name(data['firstName'], data['lastName'])
    if student:
        for s in student:
            return jsonify(student), 200
    return jsonify(error='No students found'), 400

@user_views.route('/account/reset-password', methods=['PUT'])
@jwt_required()
def reset_password():
    data = request.json
    staff = update_password(data['staffID'], data['new_password'])
    if staff:
        return jsonify(message='Password reset successful'), 201
    return jsonify(error='Password reset failed'), 400

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)