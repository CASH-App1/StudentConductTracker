from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

from App.controllers import (
    create_user,
    jwt_authenticate, 
    get_all_users,
    get_all_users_json,
    jwt_required
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/post', methods=['POST'])
@login_required
def log_review():
    data = request.json
    review = log_review(data['studentID'], data['review'], data['type'])
    if review:
        return jsonify(message = 'Review logged successfully'), 200
    return jsonify(error='Invalid type'), 400


@user_views.route('/view/student', methods=['GET'])
@login_required
def view_student():
    data = request.json
    student = get_student(data['studentID'])
    if student:
        return jsonify(student), 200
    return jsonify(error='Student not found'), 400

@user_views.route('/view/student/review', methods=['GET'])
@login_required
def view_review():
    data = request.json
    student = get_student(data['studentID'])
    if student:
        review = get_review(data['reviewID'])
        if review:
            return jsonify(review), 200
        return jsonify(error='Review not found'), 400
    return jsonify(error='Student not found'), 400


@user_views.route('/add-student', methods=['POST'])
@login_required
def add_student():
    data = request.json
    student = add_student(data['studentID'], data['firstName'], data['lastName'])
    if student:
        return jsonify(message='Student added successfully'), 200
    return jsonify(error='A student already exists with this ID'), 400

@user_views.route('/update-student', methods=['PUT'])
@login_required
def update_student():
    data = request.json
    student = update_student(data['studentID'], data['firstName'], data['lastName'])
    if student:
        return jsonify(message='Student updated successfully'), 200
    return jsonify(error='Update unsuccessful'), 400


@user_views.route('/search', methods=['GET'])
@login_required
def search_student():
    data = request.json
    student = get_all_students(data['firstName'], data['lastName'])
    if student:
        for s in student:
            return jsonify(student), 200
    return jsonify(error='No students found'), 400

@user_views.route('/account/reset-password', methods=['PUT'])
@login_required
def reset_password():
    data = request.json
    staff = update_password(data['staffID'], data['new_password'])
    if staff:
        return jsonify(message='Password reset successful'), 200
    return jsonify(error='Password reset failed'), 400
