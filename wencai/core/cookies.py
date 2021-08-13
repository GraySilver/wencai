import os
import json
import execjs
import datetime as dt


class WencaiCookie:

    def __init__(self):
        self.json_path = os.path.dirname(__file__) + '/cookies.json'

    def getHeXinVByHttp(self):
        with open(os.path.dirname(os.path.dirname(__file__)) + '/js/hexin.js', 'r') as f:
            jscontent = f.read()
        context = execjs.compile(jscontent)
        return context.call("v")

    def setHexinByJson(self, source, cookies=None):
        if cookies is None: cookies = dict()
        henxin_v = self.getHeXinVByHttp()
        cookies[source] = henxin_v
        cookies['expire_time'] = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.json_path, 'w') as f:
            json.dump(cookies, f)
        return henxin_v

    def is_expire(self, expire_time, days=3):
        delta = dt.datetime.today() - dt.datetime.strptime(expire_time, '%Y-%m-%d %H:%M:%S')
        if delta.days >= days:
            return True
        else:
            return False

    def getHexinVByJson(self, source):
        json_path = os.path.dirname(__file__) + '/cookies.json'
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                cookies = json.load(f)

            if source in cookies:
                if not self.is_expire(cookies['expire_time']):
                    return cookies[source]
                else:
                    return self.setHexinByJson(source=source, cookies=cookies)
            else:
                return self.setHexinByJson(source=source, cookies=cookies)
        else:
            self.setHexinByJson(source=source)
