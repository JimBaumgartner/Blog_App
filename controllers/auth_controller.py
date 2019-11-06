# login, logout, register
from flask import Blueprint, request

auth_blueprint = Blueprint('auth_api', __name__)


# login route
@auth_blueprint.route('/login', methods=['POST'])
def login():
    
    # to log the user in and return an authintication token
    # body name { username, password }
    #return  {auth_token} 
    body = request.json
    print(body['email'], body['password'])
    return {
        'author_token': 'qwertyyuiyioiu'
    }

# logout route
@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    #de-authinticatr the token
    return 'logout route hit'

# register route
@auth_blueprint.route('/login', methods=['POST'])
def register():
    # Create a user
    # Body :  {email, password, first_name, last_name }
    # Return  { message }
    body = request.json

    print(body['email'], body['password'], body['f_name'], body['l_name'])    

    return {
        'message': 'User Succesfully created'
    }

