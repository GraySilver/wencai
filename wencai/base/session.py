# -*- coding:utf-8 -*-
import requests


class Session:

    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }

    def __call__(self):
        self.session = requests.Session()
        self.session.headers.update(Session.headers)
        return self.session

