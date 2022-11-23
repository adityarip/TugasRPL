import csv

def getCurrentLog() -> str: #mengambil logid dari user_log.csv
    with open("./src/data/user_log.csv","r",newline="") as userLog:
        readLog = csv.reader(userLog, delimiter=";")
        for row in readLog:
            logid = row[0]
    return logid

def getCurrentUser() -> str: #mengambil userid dari user_log.csv
    with open("./src/data/user_log.csv","r",newline="") as userLog:
        readLog = csv.reader(userLog, delimiter=";")
        for row in readLog:
            userid = row[1]
    return userid

def getCurrentKas() -> str: #mengambil value kasid dari user_log.csv
    with open("./src/data/user_log.csv","r",newline="") as userLog:
        readLog = csv.reader(userLog, delimiter=";")
        for row in readLog:
            kasid = row[2]
    return kasid

def setCurrentKas(kasid: int): #mengubah value kasid dari user_log.csv
    with open("./src/data/user_log.csv","r",newline="") as f:
        reader = csv.reader(f, delimiter=";")
        rows = list(reader)
        rows[len(rows) - 1][2] = kasid

    with open("./src/data/user_log.csv", "w",newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(rows)
