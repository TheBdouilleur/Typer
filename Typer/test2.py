import datetime
date = str(datetime.date.today().strftime("%B %d, %Y"))
time = str(datetime.datetime.now().time())
datetime = date + ', at ' + time +', in typr.py:'
print(datetime)