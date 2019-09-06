from db import models

def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    course_list = teacher_obj.check_course()
    if course_list:
        return True, course_list
    return False, '没有课程'

def choose_course_interface(teacher_name, course_name):
    teacher_obj = models.Teacher.select(teacher_name)
    if course_name in teacher_obj.teacher_course_list:
        return False, '课程已存在'
    teacher_obj.choose_course(course_name)
    return True, f'{course_name}---课程添加成功'
def check_student_interface(teacher_name, course_name):
    teacher_obj = models.Teacher.select(teacher_name)
    student_list = teacher_obj.check_student(course_name)
    if student_list:
        return True, student_list

    return False, '课程下没有学生'
def change_score_interface(username, course_name, student_name, score):
    teacher_obj = models.Teacher.select(username)
    teacher_obj.change_score(course_name, student_name, score)
    return True, '修改成绩成功'
