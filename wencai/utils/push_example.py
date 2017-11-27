import os,sys
from wencai.utils.template import classMailer
import wencai as wc
import pandas as pd
import warnings
pd.set_option('display.max_colwidth', 1000)
warnings.filterwarnings('ignore')


class Pusher:

    def is_push(self,today):
        stime = str((dt.datetime.strptime(today,'%Y-%m-%d')-dt.timedelta(30)).strftime('%Y-%m-%d'))
        etime = today
        hold_for = 3
        lowerIncome = 10
        upperIncome = 6
        fell = 0.001
        fallIncome = 6
        stockHoldCount = 2

        resp = wc.get_scrape_transaction(query='主力资金流入前10',stime=stime,etime=etime,
                               hold_for=hold_for,lowerIncome=lowerIncome,
                               upperIncome=upperIncome,fell=fell,fallIncome=fallIncome,stockHoldCount=stockHoldCount)
        return resp

    def send_email(self,today,to_email):
        mailer = classMailer()
        data = self.is_push(today=today)
        if data is False:
            print('当天无邮件')
        else:
            print(data)
            html_text = mailer.html_mould(df=data,index_name='日期',first_text='xx')
            mailer.mail_set(html_text,'输出'%today,to_email=to_email)

            return html_text

if __name__ == '__main__':
    import datetime as dt
    today = str(dt.date.today())
    pusher = Pusher()
    r = pusher.is_push(today)
    print(r)
    # pusher.send_email(today,to_email='xxx')
