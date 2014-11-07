__author__ = 'hyphen'
import urllib,urllib2,cookielib
def test():
# for mail.sina.com.cn

    cj = cookielib.CookieJar()
    url_login = 'http://console.plcloud.com/auth/login/'
    data = {'csrfmiddlewaretoken':'3Nmh7gK9dkPYGfEz09h2Ft4ySQf3AX9r',\
        'password':'Zm1wbGNs','region':'http://58.67.194.89:5001/v2.0',\
         'username':'yanheven@gmail.com'}
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #opener.addheaders = [('User-agent', 'Opera/9.23')]
    opener.addheaders = [('User-agent',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:32.0) Gecko/20100101 Firefox/32.0')]
    opener.addheaders = [('X-CSRFToken','3Nmh7gK9dkPYGfEz09h2Ft4ySQf3AX9r'),\
                         ('Connection','keep-alive'),\
                         ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                         ('Cookie','sessionid=73434f5ea4f69950466c42e5b3380489; csrftoken=3Nmh7gK9dkPYGfEz09h2Ft4ySQf3AX9r')]
    urllib2.install_opener(opener)
    req=urllib2.Request(url_login,urllib.urlencode(data))
    u=urllib2.urlopen(req)
    print u.read()
        #.decode('utf-8').encode('gbk')

test()