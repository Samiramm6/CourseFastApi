# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InputFile
# import aiogram.utils
# from sqlalchemy.orm import Session
# from testservice import get_lesson_with_video
# from db import get_db
# import os
#
# # Токен твоего бота
# API_TOKEN = '7409414384:AAHDjhLqA-fVN0hlGOt9lfnN8aY7ZJx0XoM'
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     await message.reply("Добро пожаловать! Введите ID урока, чтобы получить видео.")
#
# @dp.message_handler()
# async def get_lesson_video(message: types.Message):
#     try:
#         lesson_id = int(message.text)
#     except ValueError:
#         await message.reply("Введите корректный ID урока.")
#         return
#
#     # Получение видео из базы данных по ID урока
#     with next(get_db()) as db:
#         lesson = get_lesson_with_video(lesson_id, db)
#
#         if lesson is None or lesson.video_id is None:
#             await message.reply("Видео для этого урока не найдено.")
#         else:
#             # Путь к видеофайлу
#             video_path = lesson.video.file_path
#
#             # Проверяем, существует ли файл
#             if not os.path.exists(video_path):
#                 await message.reply("Видео не найдено на сервере.")
#                 return
#
#             # Отправляем видео пользователю
#             video = InputFile(video_path)
#             await bot.send_video(message.chat.id, video, caption=f"Видео для урока: {lesson.title}")
