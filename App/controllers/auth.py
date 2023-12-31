from flask_login import login_user, login_manager, logout_user, LoginManager
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

from App.models import StaffMember

def jwt_authenticate(username, password):
  staff = StaffMember.query.filter_by(username=username).first()
  if staff and staff.check_password(password):
    return create_access_token(identity=username)
  return None

def login(username, password):
    staff = StaffMember.query.filter_by(username=username).first()
    if staff and staff.check_password(password):
        return staff
    return None

def setup_flask_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return StaffMember.query.get(user_id)
    
    return login_manager

def setup_jwt(app):
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        staff = StaffMember.query.filter_by(username=identity).one_or_none()
        if staff:
            return staff.staffID
        return None

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return StaffMember.query.get(identity)

    return jwt
