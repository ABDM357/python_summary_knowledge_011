from db import models
def register_interface(username, pwd):
    student_obj = models.Student.select(username)
    if student_obj:
        return False, '已经注册'
    models.Student(username, pwd)
    return True, f'{username}注册成功'

def choose_school_interface(student_name, school_name):
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False,'学生已经选择学校'
    student_obj.choose_school(school_name)
    return True, f'{student_name}选择学校成功'

def get_course_interface(username):
    student_obj = models.Student.select(username)

    if student_obj.school:
        school_name = student_obj.school
        school_obj = models.School.select(school_name)
        return True,school_obj.school_course_list
    return False, '请先选择学校'

def choose_course_interface(student_name, course_name):
    student_obj = models.Student.select(student_name)

    if course_name in student_obj.student_course_list:
        return False, '课程已经选择过了'
    student_obj.choose_school(course_name)
    return True, f'{course_name}选择课程成功'

def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    score_dic = student_obj.check_score()
    return score_dic