#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa when start by N
"""

if __name__ == '__main__':
    import MySQLdb as sql
    from sys import argv as par

    log = sql.connect(host='localhost', user=par[1], passwd=par[2], db=par[3])

    cur = log.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    log.close()
