from maxmeter import MaxMeter
from os import environ
from random import randrange
import schedule
import time

def task_meter():
    MaxMeter.position('EAGLEUK', 'WOKING')
    MaxMeter.login(environ['APP_KEY'], environ['APP_URL'])
    assetnum  = environ['APP_PREFIX'] + '1'
    metername = environ['APP_PREFIX'] + 'COUNT1'
    car1 = MaxMeter(assetnum, metername, str(randrange(150))) 
    # print(car1.getData())
    print('Run task_meter: ', time.ctime(time.time()) )
    print(car1.post().content)

print('Start cron: ', time.ctime(time.time()) )
schedule.every().day.at('21:30').do(task_meter)

while 1:
    schedule.run_pending()
    time.sleep(1)
