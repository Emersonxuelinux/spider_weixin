# -*- coding: utf-8 -*-
from url_info import *
from spider import *
import itchat
from sleep import *
from datetime import datetime

sleep()
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print msg['Text']

itchat.auto_login(hotReload=True)
itchat.run

curTime = datetime.now().strftime('%y-%m-%d')
itchat.send(curTime, 'filehelper')

for (name, fund_id) in ids.items():
    url = 'http://fund.eastmoney.com/%s.html' % fund_id
    value = spider(url)
    sign = value[0]
    value_num = value[1:-1]
    name = name.decode('utf-8')
    if(sign == '-' and float(value_num)>2.5):
        content = u'%s跌幅很大，可以补仓'+sign+value_num
        itchat.send(content % name, 'filehelper')
    else:
        content = u'%s 不需要补仓'+sign+value_num
        itchat.send(content % name, 'filehelper')




