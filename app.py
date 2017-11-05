from tinydb import TinyDB, Query
from datetime import time
from datetime import date
from datetime import datetime

db = TinyDB('rfid.json')

def save_tag(tag):
    db_date = date.today()
    db_time = datetime.time(datetime.now())
    db.insert({'rfid': tag, 'date': str(db_date), 'time': str(db_time)})

def get_tags():
    for tag in db.all():
        print(tag['rfid'])

def print_menu():
    print "-" * 30
    print "1) Save Tag"
    print "2) List All Tags"
    print "3) Exit"

if __name__ == "__main__":
    while True:
        print_menu()
        action = raw_input("> ")
        if action == "1":
            tag = raw_input("ID: ")
            save_tag(tag)
        elif action == "2":
            get_tags()
        elif action == "3":
            exit()
        else:
            print "Bad Command"