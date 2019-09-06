from interface import admin_interface, common_interface
from lib import common
admin_info = {'user': None}
def register():
    while True:
        username = input('请输入管理员名字：').strip()
        pwd = input('请输入管理员密码：').strip()
        re_pwd = input('请再一次确认密码：').strip()
        if pwd == re_pwd:
            flag, msg = admin_interface.register_interface(username, pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')
def login():
    while True:
        username = input('请输入管理员名字：').strip()
        pwd = input('请输入管理员密码：').strip()
        flag, msg = common_interface.login_interface(username, pwd, user_type = 'admin')
        if flag:
            print(msg)
            admin_info['user'] = username
            break
        else:
            print(msg)
@common.login_auth('admin')
def create_school():
    while True:
        school_name = input('请输入学校名字：').strip()
        school_addr = input('请输入学校地址：').strip()
        flag, msg = admin_interface.create_school_interface(admin_info.get('user'), school_name, school_addr)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入老师名字：').strip()
        flag, msg = admin_interface.create_teacher_interface(admin_info['user'], teacher_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth('admin')
def create_course():
        while True:
            school_list = common_interface.get_school_interface()
            if not school_list:
                print('没有创建学校')
                break
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
            course_name = input('请输入创建的课程名字：').strip()
            flag, msg = admin_interface.create_course_interface(admin_info['user'], school_name, course_name)
            if flag:
                print(msg)
                break
            else:
                print(msg)



func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_teacher,
    '5': create_course,
}
def admin_view():
    while True:
        print("""
        1. 注册
        2. 登录
        3. 创建学校
        4. 创建老师
        5. 创建课程
        q. 退出
        """)
        choice = input('请输入你的选择，否则q退出：').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print('输入不对')
            continue
        func_dic.get(choice)()