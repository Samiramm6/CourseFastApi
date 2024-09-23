from sqlalchemy.orm import joinedload
from db import get_db
from db.models import Courses, Lessons, Cart

def add_course_db(title, desc):
    with next(get_db()) as db:
        create_course = Courses(title=title, desc=desc)
        db.add(create_course)
        db.commit()
        return "Курс добавлен"

def get_all_courses_db():
    with next(get_db()) as db:
        all_courses = db.query(Courses).all()
        return all_courses

def get_exact_course_db(course_id):
    with next(get_db()) as db:
        exact_course = db.query(Courses).filter_by(id=course_id).first()
        if exact_course:
            return exact_course
        return False

def change_course_info_db(course_id, change_info, new_info):
    with next(get_db()) as db:
        course = db.query(Courses).filter_by(id=course_id).first()
        if course:
            if change_info == "title":
                course.title = new_info
            elif change_info == "desc":
                course.desc = new_info
            db.commit()
            return True
        return "Неверные данные"



def del_exact_course_db(course_id):
    with next(get_db()) as db:
        del_exact_course = db.query(Courses).filter_by(id=course_id).first()
        if del_exact_course:
            db.delete(del_exact_course)
            db.commit()
            return del_exact_course
        return False


def add_lesson_db(title, desc, price, course_id):
    with next(get_db()) as db:
        course = db.query(Courses).filter_by(id=course_id).first()
        if not course:
            return "Курса с данным id не существует"
        new_lesson = Lessons(title=title, desc=desc, price=price, course_id=course_id)
        db.add(new_lesson)
        db.commit()
        return new_lesson


def change_lesson_db(lesson_id, change_info, new_info):
    with next(get_db()) as db:
        lesson = db.query(Lessons).filter_by(id=lesson_id).first()

        if not lesson:
            return "Урок с данным id не найден"
        if change_info == "title":
            lesson.title = new_info
        elif change_info == "desc":
            lesson.desc = new_info
        elif change_info == "price":
            lesson.price = new_info
        elif change_info == "course_id":
            course = db.query(Courses).filter_by(id=new_info).first()
            if not course:
                return "Курса с данным id не существует"
            lesson.course_id = new_info
        else:
            return "Недопустимое поле для изменения"
        db.commit()
        return "Информация успешно изменена"


def all_lessons_db():
    with next(get_db()) as db:
        all_lessons = db.query(Lessons).options(joinedload(Lessons.videos)).all()
        return all_lessons


def add_to_cart_db(lessons_id):
    with next(get_db()) as db:
        add_to_cart = db.query(Lessons).filter_by(id=lessons_id).first()
        if add_to_cart:
            return "Добавлено в корзину"
        return False

def change_cart_db(lesson_id):
    with next(get_db()) as db:
        change_cart = db.query(Lessons).filter_by(id=lesson_id).first()
        return change_cart


def delete_lesson_db(lessons_id):
    with next(get_db()) as db:
        delete_lesson = db.query(Lessons).filter_by(id=lessons_id).first()
        if delete_lesson:
            db.delete(delete_lesson)
            db.commit()
            return delete_lesson
        return False

