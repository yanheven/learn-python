__author__ = 'hyphen'
import cookielib
import urllib2
import urllib
# first url request
baiduSpaceEntryUrl = "http://hi.baidu.com/motionhouse";
cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
urllib2.install_opener(opener);
resp = urllib2.urlopen(baiduSpaceEntryUrl);

# second time do url request, the cookiejar will auto handle the cookie
loginBaiduUrl = "https://passport.baidu.com/?login";
para = {
    'csrfmiddlewaretoken':'3Nmh7gK9dkPYGfEz09h2Ft4ySQf3AX9r',
    'region':'http%3A%2F%2F58.67.194.89%3A5001%2Fv2.0',
    'username':'yanheven%40gmail.com',
    'password':'Zm1wbGNs',
    };
postData = urllib.urlencode(para);
req = urllib2.Request(loginBaiduUrl, postData); # urllib2.Request: the HTTP request will be a POST instead of a GET when the data parameter is provided.
req.add_header('User-Agent', gConst['userAgentIE9']);
req.add_header('Content-Type', 'application/x-www-form-urlencoded');
req.add_header('Cache-Control', 'no-cache');
req.add_header('Accept', '*/*');
req.add_header('Connection', 'Keep-Alive');
resp = urllib2.urlopen(req);
respInfo = resp.info();