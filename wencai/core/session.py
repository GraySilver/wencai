# -*- coding:utf-8 -*-
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Session(requests.Session):
    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        'Connection': 'keep-alive',
        'Content-Length': "738",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest"

    }

    def __init__(self, hexin_v=None, update_headers=None):
        requests.Session.__init__(self)
        self.headers.update(Session.headers)
        self.headers['hexin-v'] = hexin_v

        if update_headers is not None and isinstance(update_headers, dict):
            for k, v in update_headers.items():
                self.headers[k] = v

    def get_driver(self, url, execute_path=None, is_headless=True):
        driver = None
        try:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            if execute_path is None:
                driver = webdriver.Chrome(chrome_options=chrome_options)
            else:
                driver = webdriver.Chrome(executable_path=execute_path, chrome_options=chrome_options)
            driver.get(url)
            return driver.page_source
        except Exception as e:
            raise IOError(e)
        finally:
            if driver is not None:
                driver.quit()
