# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')

msg = MIMEText('<html><body><h1>你好，我是乐薇，这个是我通过python发送的邮件。</h1>' +
    '<p>祝你新年快乐! <a href="https://image.baidu.com/search/detail?ct=503316480&z=0&tn=baiduimagedetail&ipn=d&cl=2&cm=1&sc=0&lm=-1&ie=gbk&pn=1&rn=1&di=195896374520&ln=30&word=happy%20new%20year&os=3192530086,3859890264&cs=682598598,3489093463&objurl=http%3A%2F%2Fhdwallpaperssys.com%2Fwp-content%2Fuploads%2F2014%2F11%2FFree-Happy-new-year-2015-3d-wallpaper.jpg&bdtype=0&simid=3342096833,189978886&pi=0&adpicid=0&timingneed=0&spn=0&is=0,0&fr=ala&ala=1&alatpl=adress&pos=1&oriquery=happy%20new%20year&hs=2&xthttps=111111">这是一个多媒体内容</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr(u'乐薇 <%s>' % from_addr)
msg['To'] = _format_addr(u'接受者 <%s>' % to_addr)
msg['Subject'] = Header(u'我是乐薇，这个我通过python发送的邮件', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
