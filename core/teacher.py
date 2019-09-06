from interface import teacher_interface, common_interface
from lib import common
teacher_info = {'user': None}
def login():
    while True:
        username = input('请输入老师名字：').strip()
        pwd = input('请输入老师密码：').strip()
        flag, msg = common_interface.login_interface(username, pwd, user_type = 'teacher')
        if flag:
            print(msg)
            teacher_info['user'] = username
            break
        else:
            print(msg)
@common.login_auth('teacher')
def check_course():
    while True:
        flag, course_list_or_msg = teacher_interface.check_course_interface(teacher_info['user'])
        if flag:
            print(course_list_or_msg)
            break
        else:
            print(course_list_or_msg)

@common.login_auth('teacher')
def choose_course():
    while True:
        course_list = common_interface.get_course_interface()
        if not course_list:
            print('没有选择课程')
            break
        for index, course in enumerate(course_list):
            print(index, course)
        choice = input('请输入你的选择,否则q退出：').strip()
        if choice == 'q':
            break
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(course_list)):
            print('超出选择范围')
            continue
        course_name = course_list[choice]
        flag, msg = teacher_interface.choose_course_interface(teacher_info['user'], course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth('teacher')
def check_student():
    while True:
        flag, course_list_or_msg = teacher_interface.check_course_interface(teacher_info['user'])
        if not flag:
            print('先选择课程')
            break
        for index, course in enumerate(course_list_or_msg):
            print(index, course)
        choice = input('请输入你的选择,否则q退出：').strip()
        if choice == 'q':
            break
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(course_list_or_msg)):
            print('超出选择范围')
        course_name = course_list_or_msg[choice]
        flag, student_flag_or_msg = teacher_interface.check_student_interface(teacher_info['user'], course_name)
        if flag:
            print(student_flag_or_msg)
            break
        else:
            print(student_flag_or_msg)

@common.login_auth('teacher')
def change_score():
    while True:
        flag, course_list_or_msg = teacher_interface.check_course_interface(teacher_info['user'])
        if not flag:
            print('先选择课程')
            break
        for index, course in enumerate(course_list_or_msg):
            print(index, course)
        choice = input('请输入你的选择,否则q退出：').strip()
        if choice == 'q':
            break
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(course_list_or_msg)):
            print('超出选择范围')
            continue
        course_name = course_list_or_msg[choice]
        flag, student_flag_or_msg = teacher_interface.check_student_interface(teacher_info['user'], course_name)
        if not flag:
            print(student_flag_or_msg)
            break
        for index, student in enumerate(student_flag_or_msg):
            print(index, student)
        choice2 = input('请输入你的选择,否则q退出：').strip()
        if choice2 == 'q':
            break
        if not choice2.isdigit():
            print('请输入数字')
            continue
        choice2 = int(choice2)
        if choice not in range(len(student_flag_or_msg)):
            print('超出选择范围')
            continue
        student_name = student_flag_or_msg[choice2]
        score = input('请选择修改的分数：').strip()
        flag, msg = teacher_interface.change_score_interface(teacher_info['user'], course_name, student_name, score)
        if flag:
            print(msg)
            break
        else:
            print(msg)

func_dic = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_student,
    '5': change_score,
}
def teacher_view():
    while True:
        print("""
        1. 登录
        2. 查看课程
        3. 选择课程
        4. 查看课程下学生
        5. 修改分数
        q. 退出
        """)
        choice = input('请输入你的选择，否则q退出：').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print('输入不对')
            continue
        func_dic.get(choice)()




