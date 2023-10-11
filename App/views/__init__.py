# blue prints are imported 
# explicitly instead of using *
from .staff import user_views
from .auth import auth_views
from .review import review_views

views = [user_views, auth_views, review_views] 
# blueprints must be added to this list