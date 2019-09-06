from db import models

def register_interface(username, pwd):
    admin_obj = models.Admin.select(username)
    if admin_obj:
        return False, '用户已经存在'
    models.Admin(username, pwd)
    return True, f'{username}注册成功'
def create_school_interface(admin_name, school_name, school_addr):

    school_obj = models.School.select(school_name)
    if school_obj:
        return False, '学校已经存在'
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name, school_addr)
    return True, f'{school_name}创建学校成功'


def create_teacher_interface(admin_name, teacher_name, teacher_pwd = '123'):

    teacher_obj = models.School.select(teacher_name)
    if teacher_obj:
        return False, '老师已经存在'
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True, f'{teacher_name}创建老师成功'

def create_course_interface(admin_name, school_name,course_name):
    admin_obj = models.Admin.select(admin_name)
    school_obj = models.School.select(school_name)
    if course_name in school_obj.school_course_list:
        return False, '学校已经存在此课程'
    admin_obj.create_course(school_name, course_name)
    return True, f'{course_name}创建课程成功'