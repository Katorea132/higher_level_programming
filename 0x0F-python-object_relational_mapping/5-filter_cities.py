#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa when start by N
"""

if __name__ == '__main__':
    import MySQLdb as sql
    from sys import argv as par

    log = sql.connect(host='localhost', user=par[1], passwd=par[2], db=par[3])

    cur = log.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM "
    query += "cities LEFT JOIN states ON cities.state_id = states.id WHERE "
    cur.execute(query + "states.name = %s ORDER BY cities.id ASC", (par[4], ))
    rows = cur.fetchall()
    print(", ".join([row[1] for row in rows]))
    cur.close()
    log.close()
