#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib import request

#define the target url
url = 'http://www.baidu.com'

# use 'request' object to send GET request
with request.urlopen(url) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))



#-----We can also insert customized field into http header-----
url = 'http://www.baidu.com'
#define the Request object and set url attribute
req = request.Request(url)
#add a header field into req(Request object)
req.add_header('User-Agent', 'Mozilla/6.0')
req.add_header('Vistor', 'MarkZhang')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:' , f.read().decode('utf-8'))
