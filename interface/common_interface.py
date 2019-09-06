from conf import settings
from db import models
import os
def get_school_interface():
    school_path = os.path.join(settings.DB_PATH, 'School')
    if os.path.exists(school_path):
        school_list = os.listdir(school_path)
        return school_list
def get_course_interface():
    course_path = os.path.join(settings.DB_PATH, 'Course')
    if os.path.exists(course_path):
        return os.listdir(course_path)
def login_interface(username, pwd, user_type):
    if user_type == 'admin':
        obj = models.Admin.select(username)
    elif user_type == 'student':
        obj = models.Student.select(username)
    elif user_type == 'teacher':
        obj = models.Teacher.select(username)
    else:
        return False, '权限不足'
    if not obj:
        return False, '用户不存在'
    if pwd == obj.pwd:
        return True, f'{username}---登录成功'
    return False, '密码不对'



