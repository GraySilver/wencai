# -*- coding:utf-8 -*-
import os
import requests


class Session:

    # headers = {
    #     'X-Requested-With': 'XMLHttpRequest',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # }

    headers = {

        "Accept":"application/json,text/javascript,*/*;q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8",
        'Connection':'keep-alive',
        'Content-Length':"738",
        'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
        # 'Cookie':"other_uid=Ths_iwencai_Xuangu_jd5locvrl7oj4cwmyxf20rwb5pj15w52; other_uname=kumldvqxvo; guideState=1; PHPSESSID=7afe79045ee8841c3fe7e47dba243396; cid=5d2jndjf36e56ob5tcalqod1j01510059317; ComputerID=5d2jndjf36e56ob5tcalqod1j01510059317; v=AlqoJedy1G4ltVjCPWtUmvu4qwtvi91SUAxSEmTSBBm4WfC3TBsudSCfohM0",
        'Host':"www.iwencai.com",
        'Origin':"http://www.iwencai.com",
        "Referer":"http://www.iwencai.com/traceback/strategy/",
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'X-Requested-With':"XMLHttpRequest"



    }


    def __call__(self):
        self.session = requests.Session()
        self.session.headers.update(Session.headers)
        self.session.headers['hexin-v'] = 'AqfarMhOsYKxkDUOHdw-koUdP9pxLHsO1QD_gnkUwzZdaMkKgfwLXuXQj9eJ'
        # with open(os.path.dirname(os.path.dirname(__file__))+'/utils/v.txt','r') as f:
        #     self.session.headers['hexin-v'] = f.read()
            # f.read()

        return self.session

