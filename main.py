from fastapi import FastAPI
from db import Base, engine
from api.user_api import user_router
from api.course_api import course_router
from api.lesson_api import lesson_router
from api.cart_api import cart_router
from payment import payment_router
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/", title="Project")
app.include_router(user_router)
app.include_router(course_router)
app.include_router(lesson_router)
app.include_router(cart_router)
app.include_router(payment_router)

