__author__ = 'hyphen'
import urllib2, urllib

header={
        'Host': 'console.plcloud.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:32.0) Gecko/20100101 Firefox/32.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://console.plcloud.com/auth/login/',
        'Cookie': 'sessionid=5753a8a825d65157e0eace7c0deb1b59; csrftoken=3Nmh7gK9dkPYGfEz09h2Ft4ySQf3AX9r',
        #Connection: keep-alive
        'X-CSRFToken': '3Nmh7gK9dkPYGfEz09h2Ft4ySQf3AX9r',
        X-Requested-With: XMLHttpRequest
        Referer: http://console.plcloud.com/project/volumes/
        Content-Length: 154
        Cookie: sessionid=5753a8a825d65157e0eace7c0deb1b59; csrftoken=3Nmh7gK9dkPYGfEz09h2Ft4ySQf3AX9r
        Connection: keep-alive
        Pragma: no-cache
        Cache-Control: no-cache


}
data = {'csrfmiddlewaretoken':'3Nmh7gK9dkPYGfEz09h2Ft4ySQf3AX9r',\
        'password':'Zm1wbGNs','region':'http://58.67.194.89:5001/v2.0',\
         'username':'yanheven@gmail.com'}
f = urllib2.urlopen(
        url     = 'http://console.plcloud.com/auth/login/',
        data    = urllib.urlencode(data),
        #header=header
        )

print f.read()