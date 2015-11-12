__author__ = 'evan'
import login
import nomore_mine

pingan_session = login.get_pingan_session()
res = pingan_session.get(nomore_mine.INDEX_URL)
print(res, res.content)