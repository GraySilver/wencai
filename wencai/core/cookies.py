import os
import json
import time
import datetime as dt
from selenium import webdriver
from wencai.core.cons import WENCAI_LOGIN_URL
from selenium.webdriver.chrome.options import Options


class WencaiCookie:

    def __init__(self, execute_path=None, is_headless=True):
        self.execute_path = execute_path
        self.is_headless = is_headless
        self.json_path = os.path.dirname(__file__)+'/cookies.json'

    def getHeXinVByHttp(self, source):
        driver = None
        try:
            chrome_options = Options()
            if self.is_headless:
                chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            if self.execute_path is None:
                driver = webdriver.Chrome(chrome_options=chrome_options)
            else:
                driver = webdriver.Chrome(executable_path=self.execute_path, chrome_options=chrome_options)

            driver.get(WENCAI_LOGIN_URL[source])
            time.sleep(5)
            cookies = driver.get_cookies()
            v = ''
            for i in cookies:
                if 'name' in i.keys():
                    if i['name'] == 'v': v = i['value']
            return v
        except Exception as e:
            print(e)
        finally:
            if driver is not None:
                driver.quit()

    def setHexinByJson(self, source, cookies=None):
        if cookies is None: cookies = dict()
        henxin_v = self.getHeXinVByHttp(source=source)
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
        json_path = os.path.dirname(__file__)+'/cookies.json'
        if os.path.exists(json_path):
            with open(json_path,'r') as f:
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