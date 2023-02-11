from maxmeter import MaxMeter
from os import environ
from random import randrange
from datetime import datetime
import schedule
import time

def task_meter():
    MaxMeter.position('EAGLEUK', 'WOKING')
    MaxMeter.login(environ['APP_KEY'], environ['APP_URL'])
    for id in ['1', '2', '3', '4', '5']:
        assetnum  = environ['APP_PREFIX'] + id
        metername = environ['APP_PREFIX'] + 'COUNT' + id
        car = MaxMeter(assetnum, metername, str(randrange(150))) 
        # print(car.getData())
        car.newreadingdate = datetime.now(timezone('Europe/Berlin')).replace(microsecond=0).isoformat()
        print('Run task_meter: ', time.ctime(time.time()) )
        print(car.post().content)

print('Start cron: ', time.ctime(time.time()) )
schedule.every().day.at('13:00').do(task_meter)

while 1:
    schedule.run_pending()
    time.sleep(1)
