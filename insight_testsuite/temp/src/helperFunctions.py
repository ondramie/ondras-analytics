#!/usr/bin/env python
import datetime as dt
        
def check_date(row, head):
    year, month, day = row[head["date"]].split('-')
    try: 
        dt.datetime(int(year),int(month),int(day))
        return(True)
    except:
        return(False)

def check_time(row, head):
    hour, mins, sec = row[head["date"]].split(':')
    try: 
        dt.datetime(int(hour),int(mins),int(sec))
        return(True)
    except:
        return(False)

def header_num(columns):
    headers = ('ip', 'date', 'time', 'cik', 'accession', 'extention')
    column_num = {x : columns.index(x) for x in headers}
    return(column_num)

def concat_dt(day, time):
    dat = [int(x) for x in day.split("-")]
    tim = [int(x) for x in time.split(':')]
    day_time = dt.datetime(dat[0], dat[1], dat[2], tim[0], tim[1], tim[2])
    return(day_time)

def output_format(key, table):
    out = ",".join([str(key), str(table[0]), \
                        str(table[1]), str(table[2]), \
                        str(table[3])]) + "\n"
    return(out)

def elements(row, head):
    ip = row[head["ip"]]
    cik = row[head["cik"]]
    date = row[head["date"]]
    time = row[head["time"]]
    date_time = concat_dt(date, time)
    acc = row[head["accession"]]
    ext = row[head["extention"]]
    return(ip, date_time, cik, acc, ext)

def sanity_check(row, head):
    #(check_date(row, head)) and (check_time(row, head)) and 
    if (len(row) >= len(head)):
        return(True)
    else:
        return(False)