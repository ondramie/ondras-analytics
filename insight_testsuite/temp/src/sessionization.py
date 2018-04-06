#!/usr/bin/env python

import sys
import collections
import pstats
import datetime as dt
from helperFunctions import header_num
from helperFunctions import elements, output_format, sanity_check 

def version3():
    hash_table = collections.OrderedDict()
    session_table = collections.OrderedDict()

    # reads inactivity time
    with open(sys.argv[2], 'r') as inactivity:
        session_time = int(inactivity.readline().rstrip())
        inactivity.close()

    # opens input log and output log
    with open(sys.argv[1], 'r') as logs, open(sys.argv[3], 'w') as output:
        head = header_num(next(logs).strip().split(','))
        for row in logs:
            row_e = row.strip().split(',')
            try:
                sanity_check(row_e, head)
                ip, date_time, cik, acc, ext = elements(row_e, head)
            except:
                continue

            while hash_table and (date_time - hash_table[list(hash_table.items())[0][0]][1]).seconds > session_time: 
                top_ip = list(hash_table.items())[0][0]
                output.write(output_format(top_ip, hash_table[top_ip]))
                hash_table.pop(top_ip)
                session_table.pop(top_ip)

            if ip in hash_table:
                if hash_table[ip][1] == date_time:
                    hash_table[ip][3] += 1
                else: 
                    duration_ip = (date_time - hash_table[ip][1]).seconds
                    if duration_ip <= session_time:
                        hash_table[ip][1] = date_time
                        hash_table[ip][2] += duration_ip
                        hash_table[ip][3] += 1
                        hash_table[ip] = hash_table.pop(ip)
            else:
                # 0 = start; 1 = end; 2 = duration; 3 = # of documents 
                hash_table[ip] = [date_time, date_time, 1,1]
                if ip not in session_table:
                    session_table[ip] = [date_time]

        for k in session_table:
            output.write(output_format(k, hash_table[k]))   

        logs.close(); output.close()


def version2():
    hash_table = collections.OrderedDict()
    session_table = collections.OrderedDict()

    # reads inactivity time
    with open(sys.argv[2], 'r') as inactivity:
        session_time = int(inactivity.readline().rstrip())
        inactivity.close()

    # opens input log and output log
    with open(sys.argv[1], 'r') as logs, open(sys.argv[3], 'w') as output:
        head = header_num(next(logs).strip().split(','))

        for row in logs:
            row_e = row.strip().split(',')
            try: 
                sanity_check(row_e, head)
                ip, date_time, cik, acc, ext = elements(row_e, head)
            except:
                continue

            while hash_table and (date_time - hash_table[hash_table.items()[0][0]][1]).seconds > session_time: 
                top_ip = hash_table.items()[0][0]
                output.write(output_format(top_ip, hash_table[top_ip]))
                hash_table.pop(top_ip)
                session_table.pop(top_ip)

            if ip in hash_table:
                if hash_table[ip][1] == date_time:
                    hash_table[ip][3] += 1
                else: 
                    duration_ip = (date_time - hash_table[ip][1]).seconds
                    if duration_ip <= session_time:
                        hash_table[ip][1] = date_time
                        hash_table[ip][2] += duration_ip
                        hash_table[ip][3] += 1
                        hash_table[ip] = hash_table.pop(ip)
            else:
                # 0 = start; 1 = end; 2 = duration; 3 = # of documents 
                hash_table[ip] = [date_time, date_time, 1,1]
                if ip not in session_table:
                    session_table[ip] = [date_time]

        for k in session_table:
            output.write(output_format(k, hash_table[k]))   

        logs.close(); output.close()


def main():
    import sys
    if sys.version_info[0] < 3:
        version2()
    else:
        version3()
    
if __name__ == "__main__":
    main()
    #import cProfile
    #import pstats
    #cProfile.run('main()', 'main.profile')
    #stats = pstats.Stats('main.profile')
    #stats.strip_dirs().sort_stats('time').print_stats()