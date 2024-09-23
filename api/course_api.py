from fastapi import APIRouter
from db.testservice import *
from api import result_message

course_router = APIRouter(prefix="/courses", tags=["Курсы"])

@course_router.post("/add-course")
async def add_course(title: str, desc: str):
    result = add_course_db(title, desc)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": "Не удалось добавить курс"}

@course_router.get("/get-courses")
async def get_courses():
    all_courses = get_all_courses_db()
    if all_courses:
        return {"status": 1, "message": all_courses}
    return {"status": 0, "message": "Не удалось подключиться к базе"}

@course_router.get("/get_exact_course")
async def get_exact_course(course_id: int):
    course = get_exact_course_db(course_id)
    if course:
        return {"status": 1, "message": course}
    return {"status": 0, "message": "Не удалось найти курс"}

@course_router.put("/change_course_info")
async def change_course_info_api(course_id: int, change_info: str, new_info: str):
    result = change_course_info_db(course_id, change_info, new_info)
    return result_message(result)

@course_router.delete("/del_exact_course")
async def del_exact_course(course_id: int):
    result = del_exact_course_db(course_id)
    if result:
        return {"status": 1, "message": "курс удален"}
    return {"status": 0, "message": "Не удалось удалить курс"}



