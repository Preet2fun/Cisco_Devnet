import schedule
import time
import datetime




def Minute():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print(str(TNOW) + "this will execute at every 1 min")

def Fixed_time():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print(str(TNOW) + "this will execute at exact define time")

def Second():
    TNOW = datetime.datetime.now().replace(microsecond=0)
    print(str(TNOW) + "this will execute at every 5 seconds three times")

schedule.every(1).minutes.do(Minute)
schedule.every().day.at("12:58").do(Fixed_time)
schedule.every().minute.at(":17").do(Second)
schedule.every().minute.at(":05").do(Second)
schedule.every().minute.at(":10").do(Second)
schedule.every().minute.at(":15").do(Second)

while True:
    schedule.run_pending()
    time.sleep(1)