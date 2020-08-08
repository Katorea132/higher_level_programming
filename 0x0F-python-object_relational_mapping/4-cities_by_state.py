#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa when start by N
"""

if __name__ == '__main__':
    import MySQLdb as sql
    from sys import argv as par

    log = sql.connect(host='localhost', user=par[1], passwd=par[2], db=par[3])

    cur = log.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM "
    query += "cities LEFT JOIN states ON cities.state_id = states.id "
    query += "ORDER BY cities.id ASC;"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    log.close()
