__author__ = 'evan'
import json

from test_project import model

def get_current_user():
    user = model.User('yan', 'haven@hpe.com')
    user = _get_user_dict(user)
    print(user)
    return user


def _get_user_dict(user):
    return dict(
        name = user.name,
        email = user.email,
        # birthday = self.birthday.isoformat()
    )

if __name__ == '__main__':
    print(get_current_user())