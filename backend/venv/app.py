from flask import Flask, request, render_template,request, jsonify,Blueprint
from application.models import *
import os
from application.config import LocalDevelopmentConfig
from flask_cors import CORS
from flask_caching import Cache
from flask import current_app as app
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies,JWTManager,verify_jwt_in_request,get_jwt
from functools import wraps
from flask_migrate import Migrate

from application.database import db
from flask_security.utils import hash_password
from datetime import timedelta
# from application.worker import celery_init_app


app = Flask(__name__)
# celery_app = celery_init_app(app)
if os.getenv('ENV', "development") == "production":
  raise Exception("Currently no production config is setup.")
else:
  print("Staring Local Development")
  app.config.from_object(LocalDevelopmentConfig)
app.app_context().push()
CORS(app)
db.init_app(app)

migrate = Migrate(app, db)


app.config["JWT_SECRET_KEY"] = "123456789" 
jwt = JWTManager(app)

app.secret_key="123456789"
with app.app_context():
    db.create_all()

cache = Cache(app)
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_HOST'] = 'localhost'  # or the hostname of your Redis server
app.config['CACHE_REDIS_PORT'] = 6379         # or the port number of your Redis server
app.config['CACHE_REDIS_DB'] = 0              # the database number (0 by default)
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'  # alternative way to set Redis URL

# Initialize the cache
def addroles():
   print("Adding Roles")
   role1=Role(id=1,name="admin")
   role2=Role(id=2,name="user")
   db.session.add(role1)
   db.session.add(role2)
   db.session.commit()

role=Role.query.filter((Role.name=="admin") | (Role.name == "user")).first()
if not role:
    addroles()

def addadmin():
    print("Adding Primary Admin")
    user=User(email="primaryadmin@gmail.com",password="1234",username="primaryadmin",role_id=1)
    db.session.add(user)
    # user.roles.append(Role.query.filter_by(id=1).first())
    db.session.commit()

check_admin = User.query.filter_by(user_name="primaryadmin").first()
if not check_admin:
    addadmin()


# <-------------------------------------------------------------------------------------------------------------------------->
# <-------------------------------------------------------------------------------------------------------------------------->
# <---------------------------------------------------------Routes----------------------------------------------------------->
# <-------------------------------------------------------------------------------------------------------------------------->
# <-------------------------------------------------------------------------------------------------------------------------->

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_administrator"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403
        return decorator
    return wrapper


@app.route('/api',methods=['GET'])
@jwt_required
# @admin_required()
def home():
    return jsonify({"message":"Hello User"})

@app.route('/api/signup', methods=['POST'])
# @admin_required()
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
            new_user = User(email=usermail,password=password,username=username,role_id=3)
            db.session.add(new_user)
            # new_user.roles.append(Role.query.filter_by(id=2).first())
            db.session.commit()
        else:
            return jsonify({"message": "Opps! Password didn't match"}), 201
        
    return jsonify({"message": "Signup successful"}), 201

@app.route('/api/login', methods=['POST'])
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
        # 'role_id': user.role_id
     }  
        access_token = create_access_token(identity=user.user_id,expires_delta = timedelta(days =1),additional_claims={"is_administrator": False})
        print(user_info)
        return jsonify({"access_token":access_token,"user_info":user_info,"message":"Success!",}), 200
    else:
        print(username, password)
        return jsonify({"message": "Invalid credentials"}), 401
    

@app.route('/api/adminlogin', methods=['POST'])
def adminlogin():
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
        # 'role_id': user.role_id
     }  
        access_token = create_access_token(identity=user.user_id,expires_delta = timedelta(days =1),additional_claims={"is_administrator": True})
        print(user_info)
        return jsonify({"access_token":access_token,"user_info":user_info,"message":"Success!",}), 200
    else:
        print(username, password)
        return jsonify({"message": "Invalid credentials"}), 401
    
@app.route('/api/logout', methods=['POST'])
@jwt_required()
# @admin_required()
def logout():
    response = jsonify({'message':'Logged out successfully'})

    unset_jwt_cookies(response)
    return response, 200






if __name__ == "__main__":

    app.run(host='0.0.0.0',port=5000, debug=True)
    