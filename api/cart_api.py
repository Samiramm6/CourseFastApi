from fastapi import APIRouter
from db.testservice import *
from api import result_message

cart_router = APIRouter(prefix="/cart", tags=["Купить"])

@cart_router.get("/add-to-cart")
async def add_to_cart_api(lessons_id: int):
    result = add_to_cart_db(lessons_id)
    return result_message(result)

# @cart_router.put("/change")
# async def change_cart_api(lesson_id)

