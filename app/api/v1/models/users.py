from werkzeug.security import safe_str_cmp


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = [
    User(1, 'username', 'password'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)