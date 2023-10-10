from App.models import StaffMember
from App.database import db

# Controller to create a staff member
def createStaff(username, password, email, firstName, lastName):
    newStaff = StaffMember(username=username, password = password, email=email, firstName=firstName, lastName=lastName)
    db.session.add(newStaff)
    db.session.commit()
    return newStaff
    
# Controller to get a staff member by username
def get_staff_by_username(username):
    return StaffMember.query.filter_by(username=username).first()

# Controller to get a staff member by ID
def get_staff(staffID):
    return StaffMember.query.get(staffID)

# Controller to get a list of all staff members
def get_all_staff():
    return StaffMember.query.all()
    
# Controller to change staff password
def update_password(staff_id, new_password):
    staff = StaffMember.query.get(staff_id)
    if staff:
        staff.password = set_password(new_password)
        db.session.add(staff)
        db.session.commit()
        return staff
    return None

def get_all_staff_json():
    staff = StaffMember.query.all()
    if not staff:
        return []
    staff = [s.get_json() for s in staff]
    return staff






