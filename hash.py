# import jwt
# from fastapi.security import OAuth2PasswordBearer
# from typing import Optional
# from db.models import User
# from db import get_db
# from datetime import timedelta
#
#
# # Функ для проверки пароля
# def verify_password(password, hashed_password):
#     return password == hashed_password
#
# # Схема для токена
# oauth = OAuth2PasswordBearer(tokenUrl="token")
#
# # Функ для получения пользователя
# def get_user(username):
#     with next(get_db()) as db:
#         user = db.query(User).filter_by(username=username).first()
#         if user in db:
#             user_dict = db[user]
#             return User(**user_dict)
#
#
# jwt token
# def crate_access_token(expire_date: Optional[timedelta] = None):
#     with next(get_db()) as db:
#         to_encode = db.query()
#
#
#
#
