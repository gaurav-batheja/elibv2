from flask_security import Security, SQLAlchemyUserDatastore
from .models import db, User, Role

security =  Security()
user_datastore = SQLAlchemyUserDatastore(db, User, Role)