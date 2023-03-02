import pytz
import datetime as dt

def get_tw_time() -> str:
    tw = pytz.timezone('Asia/Taipei')
    twdt = tw.localize(dt.datetime.now()).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return twdt