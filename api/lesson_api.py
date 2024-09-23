import os
from api import result_message
from fastapi import APIRouter, File, UploadFile, Depends
from db.testservice import *
from sqlalchemy.orm import Session
from db.models import Video
import random

lesson_router = APIRouter(prefix="/lessons", tags=["Уроки"])


@lesson_router.post("/add_videos")
async def add_videos(lesson_id: int, video_files: list[UploadFile] = File(...), db: Session = Depends(get_db)):
    saved_files = []
    for video_file in video_files:
        file_id = random.randint(1, 100000000)
        file_name = f"video_{file_id}_{lesson_id}.mp4"
        file_path = os.path.join("db", "video", file_name)

        with open(file_path, "wb") as file:
            video_to_save = await video_file.read()
            file.write(video_to_save)

        new_video = Video(
            lesson_id=lesson_id,
            file_path=file_path
        )
        db.add(new_video)
        saved_files.append(file_name)

    db.commit()
    return {"status": 1, "message": "Видео успешно загружены"}

@lesson_router.post("/add_lesson")
async def add_lesson_api(title: str, desc: str, price: float, course_id: int):
    result = add_lesson_db(title, desc, price, course_id)
    return result_message(result)

@lesson_router.get("/all-lessons")
async def all_lessons_api():
    result = all_lessons_db()
    return result

@lesson_router.put("/change_lesson")
async def change_lesson_api(lesson_id: int, change_info: str, new_info: str):
    result = change_lesson_db(lesson_id, change_info, new_info)
    return result_message(result)

@lesson_router.delete("/delete-lesson")
async def del_lesson_api(lessons_id: int):
    result = delete_lesson_db(lessons_id)
    return result_message(result)