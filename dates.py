import datetime


def ms_to_dt(ms):
    return datetime.datetime.fromtimestamp(ms / 1000.0)


def dt_to_ms(dt):
    return ((dt - datetime.datetime.utcfromtimestamp(0)).total_seconds() * 1000.0) - 21600000
