from db import get_db
from db.models import User


def check_user_db(username, phone_number, email):
    with next(get_db()) as db:
        check_username = db.query(User).filter_by(username=username).first()
        check_phone_number = db.query(User).filter_by(phone_number=phone_number).first()
        check_email = db.query(User).filter_by(email=email).first()
        if check_username:
            return "Юзернейи занят"
        if check_phone_number:
            return "Телефон номер занят"
        if check_email:
            return "Почта занята"
        return True


def register_user_db(username, phone_number, email, password):
    with next(get_db()) as db:
        checker = check_user_db(username, phone_number, email)
        if checker == True:
            new_user = User(username=username, phone_number=phone_number,
                            email=email, password=password)
            db.add(new_user)
            db.commit()
            return new_user


def login_user_db(login, password):
    with next(get_db()) as db:
        login_by_phone = db.query(User).filter_by(phone_number=login).first()
        login_by_email = db.query(User).filter_by(email=login).first()
        if login_by_phone:
            if login_by_phone.password == password:
                return login_by_phone.id
        elif login_by_email:
            if login_by_email.password == password:
                return login_by_email.id
        return "Неверные данные"


def profile_info_db(user_id):
    with next(get_db()) as db:
        user = db.query(User).filter_by(id=user_id).first()
        if user:
            return user
        return False


def change_user_db(user_id, change_info, new_info):
    with next(get_db()) as db:
        user = db.query(User).filter_by(id=user_id).first()
        if user:
            if change_info == "username":
                user.username = new_info
            elif change_info == "phone_number":
                user.phone_number = new_info
            elif change_info == "email":
                user.email = new_info
            elif change_info == "password":
                user.password = new_info
            db.commit()
            return True
        return "Неверные данные"


def delete_user_db(user_id):
    with next(get_db()) as db:
        user_to_delete = db.query(User).filter_by(id=user_id).first()
        if user_to_delete:
            db.delete(user_to_delete)
            db.commit()
            return True
        return "Неверный id"