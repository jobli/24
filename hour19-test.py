import sqlite3

conn = sqlite3.connect("inventory.db")
cursor2 = conn.cursor()
sql = '''SELECT * FROM ingredients WHERE title="beef"'''
#sql = '''DELETE FROM ingredients WHERE title="beef"'''
results = cursor2.execute(sql)
#conn.commit()
print results.fetchall()
