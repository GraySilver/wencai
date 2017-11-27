import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from bs4 import BeautifulSoup
from base64 import b64encode
import email
from email.utils import formataddr

class lyemail():

    """提供参数headers，title,context,filepath;
       1、 headers = {'user':'**',
           'pwd':'**',
           'to':['**','**'],
           'toaddrs':['**','**']
           }
       2、title、context must be str
       3、filepath must be correct path file on computer，默认为None，type must be str.
       4、有必要改stmp和port，请在py里修改

    """

    def __init__(self,headers,title,context,filepath=None,format='html'):
        """

        :param headers: headers
        :param title: title
        :param context: context
        :param filepath: filepath
        :param format: format
        """
        self.user = headers['user']
        self.pwd = headers['pwd']
        self.to = headers['to']
        try:
            self.toaddrs = headers['toaddrs']
        except:
            self.toaddrs = []
        self.title = title
        self.context = context
        self.filepath = filepath
        self.format = format      #格式有plain和html可选，默认html
        self.stmp = 'smtp.qq.com'  #stmp
        self.port = 465  #port

#========================
    def write_email(self):
        try:

            msg = MIMEMultipart()
            mail_configure = {}
            mail_configure['mail_encoding'] = 'utf-8'
            # msg['Subject'] =formataddr((self.title,str(self.title)))
            msg['Subject'] = self.title
            msg['From'] = formataddr((self.user,str(self.user)))
            msg['To'] = formataddr(((';'.join(self.to),str(','.join(self.to)))))
            msg['Cc'] = formataddr(((';'.join(self.toaddrs),str(','.join(self.toaddrs)))))

            # fixed_text = '发件人:'+self.user+';\n'+'收件人:'+",".join(self.to)+';\n'+'抄送:'+",".join(self.toaddrs)+';\n'
            Content = MIMEText(self.context, self.format, 'utf-8')
            msg.attach(Content)
            return msg
        except:
            print('Error:邮件格式错误，请重试')
            exit()

# ========================
    def gofile(self):
        msg = self.write_email()
        if self.filepath != None:
            attfile = self.filepath  #文件传输路径
            basename = os.path.basename(attfile)
            try:
                fp = open(attfile, 'rb')
                att = MIMEText(fp.read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', basename))
                encoders.encode_base64(att)
                msg.attach(att)
            except IOError:
                print('Error:没有找到文件或读取文件失败')
                exit()
        return msg



#============================


    def send_myself(self):
        try:
            msg = self.gofile()
            # toaddrs = self.cc
            s = smtplib.SMTP_SSL(self.stmp,self.port)
            s.login(self.user, self.pwd)
            s.sendmail(self.user, self.user, msg.as_string())
            print('邮件备份完成')
            return True
        except:
            print('Error:邮件备份失败，请重试')
            exit()


    def send_email(self):
        if self.send_myself():
            try:
                msg = self.gofile()
                # toaddrs = self.cc
                s = smtplib.SMTP_SSL(self.stmp,self.port)
                s.login(self.user, self.pwd)
                list_email = self.to + self.toaddrs
                # list_email = self.to
                s.sendmail(self.user, list_email, msg.as_string())
                print('邮件已发送')
                s.close()
            except smtplib.SMTPException:

                print('Error:邮件发送失败，请重试')
                exit()


def htmltext(html_path):
    try:
        html_text = open(html_path,'r')
        soup_text = BeautifulSoup(html_text, 'lxml')
        context = soup_text.prettify()
        # print(context)
        return context

    except IOError:
        print('Error:Html没有找到或读取失败')




def htmltext_admin(html_path):
    try:
        html_text = open(html_path, 'r')
        check_html = html_text.read()
        check_html = check_html.replace('</html_result><html_result>', '')
        return check_html

    except IOError:
        print('Error:Html没有找到或读取失败')





"""
    eg:
    headers = {'user':'**',
           'pwd':'**',
           'to':['**','**']}
    title = 'good'
    htmltext = lyemail.htmltext('**')
    parm = lyemail.lyemail(headers,title,htmltext)
    lyemail.lyemail.send_email(parm)

    """