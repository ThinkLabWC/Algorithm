from datetime import date, datetime, timezone, timedelta

exp_day = str(date.today())

KST = timezone(timedelta(hours=9))
time_record = datetime.now(KST)
_day = str(time_record)[:10]
_time = str(time_record.time())[:8]

print(_day)