import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()
sql = "select * from ingredients"
results = cursor.execute(sql)
all_ingredients = results.fetchall()
for ingredient in all_ingredients:
    print ingredient
