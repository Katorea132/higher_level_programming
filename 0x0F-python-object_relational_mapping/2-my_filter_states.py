#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa when start by N
"""

if __name__ == '__main__':
    import MySQLdb as sql
    from sys import argv as par

    log = sql.connect(host='localhost', user=par[1], passwd=par[2], db=par[3])

    cur = log.cursor()
    query = "SELECT * FROM states WHERE name "
    query += "LIKE BINARY '{}' ORDER BY id ASC".format(par[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    log.close()
