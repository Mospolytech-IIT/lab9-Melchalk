from sqlalchemy.orm import Session
from models import User

def add_several_users(db:Session):
    db.add(User(username="Mel", email="mel.mail", password="123"))
    db.add(User(username="Max", email="max.mail", password="123"))
    db.add(User(username="Katy", email="cat.mail", password="123"))

    db.commit()

def add_user(username, email, password, db:Session):
    db.add(User(username=username, email=email, password=password))
    db.commit()

def get_all_users(db:Session):
    return db.query(User).all()

def update_email(user_id, new_email, db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    user.email = new_email
    db.commit()

def delete_user(user_id, db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()