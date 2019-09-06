from interface import student_interface, common_interface
from lib import common
student_info = {'user': None}
def register():
    while True:
        username = input('请输入学生名字：').strip()
        pwd = input('请输入学生密码：').strip()
        re_pwd = input('请再一次确认密码：').strip()
        if pwd == re_pwd:
            flag, msg = student_interface.register_interface(username, pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
def login():
    while True:
        username = input('请输入学生名字：').strip()
        pwd = input('请输入学生密码：').strip()
        flag, msg = common_interface.login_interface(username, pwd, user_type = 'student')
        if flag:
            print(msg)
            student_info['user'] = username
            break
        else:
            print(msg)


@common.login_auth('student')
def choose_school():
    while True:
        school_list = common_interface.get_school_interface()

        for index, school in enumerate(school_list):
            print(index, school)
        choice = input('请输入你的选择,否则q退出：').strip()
        if choice == 'q':
            break
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            print('超出选择范围')
            continue
        school_name = school_list[choice]
        flag, msg = student_interface.choose_school_interface(student_info['user'], school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth('student')
def choose_course():
    while True:
        flag, course_list_or_msg = student_interface.get_course_interface(student_info['user'])
        if not flag:
            print(course_list_or_msg)
            break
        if not course_list_or_msg:
            print('没有课程')
            break
        for index, school in enumerate(course_list_or_msg):
            print(index, school)
        choice = input('请输入你的选择,否则q退出：').strip()
        if choice == 'q':
            break
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(course_list_or_msg)):
            print('超出选择范围')
        course_name =course_list_or_msg[choice]
        flag, msg = student_interface.choose_course_interface(student_info['user'], course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)




@common.login_auth('student')
def check_score():
    while True:
        score_dic = student_interface.check_score_interface(student_info['user'])
        print(score_dic)


func_dic = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,
}
def student_view():
    while True:
        print("""
        1. 注册
        2. 登录
        3. 选择学校
        4. 选择课程
        5. 查看分数
        q. 退出
        """)
        choice = input('请输入你的选择，否则q退出：').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print('输入不对')
            continue
        func_dic.get(choice)()