#models are our blueprints
#pythons modeling of our data in database
# attributes are going to be our columns , seperated by id , key password

from app import db
import datetime

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Interger, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    pw = db.Column(db.String(300), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50))
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def  __init__(self, email,password,first_name,last_name=None):
        self.email = email
        self.pw = password
        self.first_name = first_name
        self.last_name = last_name
        self.date_created = datetime.datetime.now()
        self.last_modified = datetime.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return 'User succesfully created'
