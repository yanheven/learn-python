from pecan import conf  # noqa


def init_model():
    """
    This is a stub method which is called at application startup time.

    If you need to bind to a parsed database configuration, set up tables or
    ORM classes, or perform any database initialization, this is the
    recommended place to do it.

    For more information working with databases, and some common recipes,
    see http://pecan.readthedocs.org/en/latest/databases.html
    """
    pass

class User(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.birthday = birthday
        self.__dict__ = self._get_user_dict()


    def _get_user_dict(self):
        return dict(
            name = self.name,
            email = self.email,
            # birthday = self.birthday.isoformat()
        )

    def __json__(self):
        return self._get_user_dict()

