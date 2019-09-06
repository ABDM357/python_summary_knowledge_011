from conf import settings
import os, pickle
def db_select(cls, username):
    class_name = cls.__name__
    dir_path = os.path.join(settings.DB_PATH, class_name)
    if os.path.isdir(dir_path):
        user_path = os.path.join(dir_path, username)
        if os.path.exists(user_path):
            with open(user_path, 'rb') as f:
                obj = pickle.load(f)
                return obj

def db_save(obj):
    class_name = obj.__class__.__name__
    dir_path = os.path.join(settings.DB_PATH, class_name)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    user_path = os.path.join(dir_path, obj.name)
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()
