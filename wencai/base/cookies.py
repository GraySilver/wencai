import os
import sys
import traceback
import time
from selenium import webdriver
from wencai.base.cons import WENCAI_URL
from selenium.webdriver.chrome.options import Options


def getHeXinVByHttp(source, execute_path=None,is_headless=True,):
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

        driver.get(WENCAI_URL[source])
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
        driver.quit()

if __name__ == '__main__':
    r = getHeXinVByHttp(source='backtest',execute_path='/Users/allen/Downloads/chromedriver')
    print(r)