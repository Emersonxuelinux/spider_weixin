# -*- coding: utf-8 -*-

from url_info import *
from spider import *
import itchat
from sleep import *

sleep()
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print msg['Text']

itchat.auto_login(hotReload=True)
itchat.run


for (name, fund_id) in ids.items():
    url = 'http://fund.eastmoney.com/%s.html' % fund_id
    value = spider(url)
    sign = value[0]
    value_num = value[1:-1]

    if(sign == '-' and float(value_num)>2.5):
        itchat.send('buy %s' % fund_id, 'filehelper')
    else:
        itchat.send('%s do not buy' % fund_id, 'filehelper')




