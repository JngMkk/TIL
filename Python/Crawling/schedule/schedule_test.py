from datetime import datetime
import schedule
import time

def job():
    now = datetime.now()
    print(now)

schedule.every().minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at('17:41').do(job)
schedule.every().monday.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)