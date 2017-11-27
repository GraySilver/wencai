from bs4 import BeautifulSoup
from ..utils.lyemail import lyemail


class classMailer:


    @staticmethod
    def html_mould(df,index_name,first_text=None):
        if len(df) == 0:
            df.index = df.pop(index_name)
            html = df.to_html()
            soup = BeautifulSoup(html, 'lxml')
            DateClear = soup.findAll('tr')[1]
            DateClear.clear()
            DateString = soup.th
            DateString.string = str(index_name)
            table = soup.table
            table['border'] = '1px'
            table['cellspacing'] = '0px'
            table['style'] = """text-align: center;
                   border-collapse: collapse; font-size: 14px;color: #333333; font-family:'微软雅黑';
                   min-width: 70px; max-width: 250px;  word-break: keep-all; white-space: nowrap;  padding: 8px;"""
            Tbody = soup.thead.tr
            Tbody['style'] = "text-align: center;"

            # charset = soup.html
            # charset['meta'] = 'http-equiv="Content-Type" content="text/html; charset=utf-8"'

            if first_text != None:
                jt_p1 = soup.body
                jt_p1_name = soup.new_tag("p")
                jt_p1.insert(0, jt_p1_name)
                jt_p1_name['style'] = 'color:red;'
                jt_p1_name.string = str(first_text) + ':'  # 需要变的地方

            Text = soup.prettify()

            return Text
        else:
            return ''




    @staticmethod
    def mail_set(text,title,to_email,headers):
        # to_email = str(to_email).split(',')
        # headers = {'user': 'xxxxxxxx',
        #            'pwd': 'xxxxxxx',
        #            'to': to_email}

        parm = lyemail(headers, title, text)
        lyemail.send_email(parm)


