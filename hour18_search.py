import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

while True:
    search = raw_input('Search for item (q to quit): ')
    if search.lower() != "q":
        search_word = (search,)
        try:
            results = cursor.execute('select * from ingredients where title=?', search_word)
            all_ingredients = results.fetchone()
            for ingredient in all_ingredients:
                print ingredient
        except:
            print '0 items found !'
    else:
        print 'Ok, quitting....'
        break
    





#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()
