from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from App.controllers import *

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
API Routes
'''
@auth_views.route('/login', methods=['POST'])
def user_login():
  data = request.json
  token = jwt_authenticate(data['username'], data['password'])
  if not token:
    return jsonify(message='Incorrect username or password'), 401
  return jsonify(token=token), 200


@auth_views.route('/signup', methods=['POST'])
def user_signup():
    data = request.json
    staff = createStaff(data['username'],data['password'],data['email'],data['firstName'], data['lastName'])
    if staff:
        return jsonify({"message" : "Account created successfully"}), 201
    return jsonify({"error":"Username already taken"}), 400

