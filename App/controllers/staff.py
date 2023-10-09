from App.models import Staff
from App.database import db

# Controller to create a staff member
def create_staff(username, password):
    new_staff = Staff(username=username, password=password)
    db.session.add(new_staff)
    db.session.commit()
    return new_staff

# Controller to get a staff member by username
def get_staff_by_username(username):
    return Staff.query.filter_by(username=username).first()

# Controller to get a staff member by ID
def get_staff(staffID):
    return Staff.query.get(staffID)

# Controller to get a list of all staff members
def get_all_staff():
    return Staff.query.all()

# Controller to update a staff member's username
def update_staff(staffID, username):
    staff = get_staff(staffID)
    if staff:
        staff.username = username
        db.session.add(staff)
        db.session.commit()
        return staff
    return None


# Controller to change staff password
def update_password(staff_id, new_password):
    staff = Staff.query.filter_by(staffID=staff_id).first()
    if staff:
        staff.password = new_password
        db.session.add(stass)
        db.session.commit()
        return staff
    return None


def get_all_staff_json():
    staff = Staff.query.all()
    if not staff:
        return []
    staff = [s.get_json() for s in staff]
    return staff



