#createing a new controller
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
blog_controller = Blueprint('blog_api', __name__)

@blog_controller.route('/new',methods=['POST'])
@jwt_required  #IF YOU ARE NOT AUTHINTICATED GET OUT
def new_blog(): #takes in nothing because it comes over in the body
  return {
    "message": "Blog post created"
  }
#then you have to register the blueprint in the init folder
  # go to __init__ folder and put this in  
#then have to go into app.py  and import 
  # from controllers import jwt, auth_blueprint, 
# then have to register the bluew print  in app.py folder  
# app.register_blueprint(blog_controller, url_prefix="/blog")