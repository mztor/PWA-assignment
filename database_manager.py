import sqlite3 as sql

def listExtension():
  con = sql.connect(".database/data_source.db")
  cur = con.cursor()
  data = cur.execute('SELECT DISTINCT area FROM restaurants').fetchall()
  print(data)
  con.close()
  return data


def getDetails(area):
  con = sql.connect(".database/data_source.db")
  cur = con.cursor()
  query = 'SELECT * FROM restaurants WHERE area = ?'
  data = cur.execute(query, [area]).fetchall()
  print(data)
  con.close()
  return data