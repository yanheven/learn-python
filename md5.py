__author__ = 'hyphen'
import hashlib
def calc_md5(passwd):
    md5=hashlib.md5()
    md5.update(passwd)
    return md5.hexdigest()


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    pass

calc_md5("fuck")

get_md5()