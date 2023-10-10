from App.models import Staff
from App.database import db

# Controller to create a staff member
def createStaff(username, password, email, firstName, lastName):
    newStaff = Staff(username=username, password=password, email=email, firstName=firstName, lastName=lastName)
    db.session.add(newStaff)
    db.session.commit()
    return newStaff
    
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
def update_staff(staffID, new_username, new_email):
    staff = get_staff(staffID)
    if staff:
        staff.username = new_username
        staff.email = new_email
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





