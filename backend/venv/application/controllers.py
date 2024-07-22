from flask import Flask, request, jsonify,Blueprint
from flask import current_app as app
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies
from .models import User
from .database import db
from flask_security import auth_required, current_user, hash_password
from flask_security.utils import hash_password
from datetime import timedelta
from flask_caching import Cache

# -------initiallize login manager--------------

# bcrypt = Bcrypt(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(id)


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/',methods=['GET'])
@jwt_required
def home():
    return [{"message":"Hello User"}]


cache=Cache(app)







@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    username = data.get('username')
    usermail = data.get('email')

    user_name=User.query.filter_by(user_name=username).first()
    user_mail=User.query.filter_by(user_mail=usermail).first()

    if user_name or user_mail:
        return jsonify({"message": "user already exists!"}), 201 
    else:
        password = data.get('password')
        passwordagain = data.get('passwordagain')

        if password == passwordagain:
            # hashed_password = hash_password(password)
            new_user = User(email=usermail,password=password,username=username)
            db.session.add(new_user)
            db.session.commit()
        else:
            return jsonify({"message": "Opps! Password didn't match"}), 201
        
    return jsonify({"message": "Signup successful"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password =  data.get('password')

    user = User.query.filter_by(user_name=username).first()

    if not user:
        print(username, password)
        return jsonify({'messgae': 'Invalid name or password'}),401

    if password==user.user_pass: 
        user_info = {
        'user_id':user.user_id,
        'username': user.user_name,
        'email':user.user_mail,
        'porfile_pic': user.user_profile_pic,
        'is_admin': user.is_admin
     }  
        access_token = create_access_token(identity=user.user_id,expires_delta = timedelta(days =1))
        print(user_info)
        return jsonify({"access_token":access_token,"user_info":user_info,"message":"Success!"}), 200
    else:
        print(username, password)
        return jsonify({"message": "Invalid credentials"}), 401
    
@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({'message':'Logged out successfully'})

    unset_jwt_cookies(response)
    return response, 200