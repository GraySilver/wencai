import os
import sys
from selenium import webdriver
from wencai.base.cons import WENCAI_URL



def getHeXinVByCookies(ktype,execute_path=None):

    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    if execute_path == None:
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        driver = webdriver.Chrome(executable_path=execute_path,chrome_options=chrome_options)

    driver.get(WENCAI_URL[ktype])
    cookies = driver.get_cookies()
    v = ''
    for i in cookies:
        if 'name' in i.keys():
            if i['name'] == 'v': v = i['value']
    driver.quit()
    return v
