from tinydb import TinyDB, Query
from datetime import time
from datetime import date
from datetime import datetime

db = TinyDB('rfid.json')

def save_tag(fc,num):
    db_date = date.today()
    db_time = datetime.time(datetime.now())
    fc_bin = str(fc_to_bin(fc))
    num_bin = str(num_to_bin(num))
    db.insert({'fc': fc_bin, 'num': num_bin, 'date': str(db_date), 'time': str(db_time)})

def get_tags():
    for tag in db.all():
        print(tag['rfid']) #Cleanup to return array

def print_menu():
    print "-" * 30
    print "1) Save Tag"
    print "2) List All Tags"
    print "3) Convert to Binary"
    print "0) Exit"

def convert_to_rfid_bin(fc,num):
    bin_fc = "0" * (8 - len(str(bin(fc))[2:])) + str(bin(fc))[2:]
    bin_num = "0" * (16 - len(str(bin(num))[2:])) + str(bin(num))[2:]
    print bin_fc
    print bin_num

def fc_to_bin(fc):
    bin_fc = "0" * (8 - len(str(bin(fc))[2:])) + str(bin(fc))[2:]
    return bin_fc

def num_to_bin(num):
    bin_num = "0" * (16 - len(str(bin(num))[2:])) + str(bin(num))[2:]
    return bin_num


if __name__ == "__main__":
    while True:
        print_menu()
        action = raw_input("> ")
        if action == "1":
            fc = int(raw_input("FC: "))
            num = int(raw_input("Number: "))
            save_tag(fc,num)
        elif action == "2":
            get_tags()
        elif action == "3":
            fc = int(raw_input("FC: "))
            num = int(raw_input("Number: "))
            print "FC: " + fc_to_bin(fc)
            print "Number: " + num_to_bin(num)
        elif action == "0":
            exit()
        else:
            print "Bad Command"