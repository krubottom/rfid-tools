from tinydb import TinyDB, Query
from datetime import time
from datetime import date
from datetime import datetime

db = TinyDB('rfid.json')

#tag = raw_input("ID: ")
db_date = date.today()
db_time = datetime.time(datetime.now())

#db.insert({'rfid': tag, 'date': str(db_date), 'time': str(db_time)})

for tag in db.all():
    print(tag['rfid'])