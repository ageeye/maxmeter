from maxmeter import MaxMeter
import schedule
import time

def task_meter():
    MaxMeter.position('EAGLEUK', 'WOKING')
    MaxMeter.login(environ['APP_KEY'], environ['APP_URL'])
    assetnum  = environ['APP_PREFIX'] + '1'
    metername = environ['APP_PREFIX'] + 'COUNT1'
    car1 = MaxMeter(assetnum, metername, str(randrange(150))) 
    # print(car1.getData())
    print(car1.post().content)

schedule.every().day.at('20:45').do(task_meter)

while 1:
    schedule.run_pending()
    time.sleep(1)
