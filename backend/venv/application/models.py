from .database import db
from flask_security import UserMixin, RoleMixin



class User(db.Model, UserMixin):
    __tablename__ = "user"
    user_id=db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_mail=db.Column(db.String(30), nullable = False, unique =True)
    
    user_pass=db.Column(db.String(30), nullable = False)
    user_name=db.Column(db.String(30),nullable= False, unique = True)
    user_profile_pic=db.Column(db.String, default = "user_profile_dummy.jpg")
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    roles = db.relationship("Role", back_populates="users")

    def __init__(self,email,password,username,role_id):
        self.user_mail=email
        self.user_pass=password
        self.user_name=username
        self.role_id=role_id

    def get_id(self):
        return self.user_id
    


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)

    users = db.relationship("User", back_populates="roles")

    def __init__(self,id,name):
        self.id=id
        self.name=name

# class UserRole(db.Model):
#     __tablename__ = "user_roles"

#     user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), primary_key=True)
#     role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), primary_key=True)
        