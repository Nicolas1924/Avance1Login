import bcrypt
from database import SessionLocal, User


def register_user(username, password, email):
    db = SessionLocal()
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    user = User(username=username, password=hashed.decode("utf-8"), email=email)
    db.add(user)
    db.commit()
    db.close()


def login_user(email, password):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()
    if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return user  # Devuelve el usuario en lugar de True
    return None
