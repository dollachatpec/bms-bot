import dbconfig
import time
def checkstatus():
    conn = dbconfig.dbcon()

    s1 = "SELECT HistoryID,StartTime,EndTime FROM alarmhistory ORDER BY HistoryID DESC LIMIT 1 ;"

    cursor = conn.cursor()
    cursor.execute(s1)
    msg = cursor.fetchall()
    sttime = time.strftime('%H:%M:%S %d-%m-%Y', time.localtime(msg[0][1]))
    endtime = time.strftime('%H:%M:%S %d-%m-%Y', time.localtime(msg[0][2]))

    msg = "Lastest History ID : "+str(msg[0][0])+" ||| Start From : "+sttime+" To "+endtime+""
    
    return msg 
