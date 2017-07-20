# -*-coding: utf-8 -*-


import time
from datetime import datetime, timedelta

SECONDS_PER_DAY = 24 * 60 * 60


def sleep():
    curTime = datetime.now()
    desTime = curTime.replace(hour=14, minute=30, second=0, microsecond=0)
    delta = desTime - curTime
    sleepTime = delta.total_seconds()
    print 'sleep:%s' % sleepTime
    time.sleep(sleepTime)
