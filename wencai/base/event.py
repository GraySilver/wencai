# -*- coding:utf-8 -*-
from wencai.base.crawler import Wencai
from wencai.utils.template import classMailer


def get_scrape_transaction(query,stime=None,etime=None,hold_for=3,stockHoldCount=2,
                           fallIncome=6,lowerIncome=10,upperIncome=6,cookies=''):
    wencai = Wencai(stime=stime,
                    etime=etime,
                    hold_for=hold_for,
                    stockHoldCount=stockHoldCount,
                    fallIncome=fallIncome,
                    lowerIncome=lowerIncome,
                    upperIncome=upperIncome,
                    cookies=cookies)

    return wencai.scrape_transaction(query)


def get_strategy(query,stime=None,etime=None,hold_for=3,stockHoldCount=2,
                           fallIncome=6,lowerIncome=10,upperIncome=6,cookies=''):
    wencai = Wencai(hold_for=hold_for,
                    stime=stime,
                    etime=etime,
                    upperIncome=upperIncome,
                    lowerIncome=lowerIncome,
                    fallIncome=fallIncome,
                    stockHoldCount=stockHoldCount,
                    cookies=cookies)
    return wencai.strategy(query)

def get_scrape_report(query,stime=None,etime=None,hold_for=3,stockHoldCount=2,
                           fallIncome=6,lowerIncome=10,upperIncome=6,cookies=''):
    wencai = Wencai(stime=stime,
                    etime=etime,
                    hold_for=hold_for,
                    stockHoldCount=stockHoldCount,
                    fallIncome=fallIncome,
                    lowerIncome=lowerIncome,
                    upperIncome=upperIncome,
                    cookies=cookies)
    return wencai.scrape_report(query)


def send_email(data,to_email,title,index_name,first_text=''):
    mailer = classMailer()
    if data is False:
        print('当天无邮件')
    else:
        print(data)
        html_text = mailer.html_mould(df=data, index_name=index_name, first_text=first_text)
        mailer.mail_set(html_text, title, to_email=to_email)
        return html_text