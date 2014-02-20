import sqlite3

def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def add_ingredient(cursor):
    ingredient = raw_input("Name of ingredient: ")
    num = raw_input("Number in storage: ")
    description = raw_input("Description: ")
    sql = '''insert into ingredients
        (title, amount, description)
        values
        ("{title}", {amount}, "{description}")'''
    sql = sql.format(title = ingredient, amount = num, description = description)
    cursor.execute(sql)
    print "Added !"

#def find_ingredient(cursor, item):
#    sql = '''SELECT title, amount FROM ingredients WHERE title="{item}"'''
#    sql = sql.format(item=item)
#    results = cursor.execute(sql)
#    items = results.fetchall()
#    if len(items == 0):
#        print "0 found !"
#    else:
#        for item in items:
#            print item[0], "-", item[1]

def find_ingredient(cursor):
    search = raw_input('Search for item: ')
    
    search_word = (search,)
    try:
        results = cursor.execute('select * from ingredients where title=?', search_word)
        all_ingredients = results.fetchone()
        for ingredient in all_ingredients:
            print ingredient
    except:
        print '0 items found !'
    
def list_ingredients(cursor):
    sql = '''SELECT title, amount FROM ingredients'''
    results = cursor.execute(sql)
    items = results.fetchall()
    print "Items in the inventory:"
    for item in items:
        print item[0], "-", item[1]

def update_ingredient(cursor):
    item = raw_input("Which item? ")
    column = raw_input("What column? (title, amount, description)? ")
    value = raw_input("To what value? ")
    if column[0].lower() == "t":
        sql = '''UPDATE ingredients
                 SET title="{value}"
                 WHERE title="{title}"'''
    elif column[0].lower() == "a":
        sql = '''UPDATE ingredients
                 SET amount="{value}"
                 WHERE title="{title}"'''
    elif column[0].lower() == "d":
        sql = '''UPDATE ingredients
                 SET description="{value}"
                 WHERE title="{title}"'''
    else:
        print "Sorry, that's not valid."
        return
    sql = sql.format(value=value, title=item)
    cursor.execute(sql)

def delete_ingredient(cursor):
    item = raw_input("Which item? ")
    confirm = raw_input("Are you sure you want to delete item? (y/n) ")
    if confirm.lower() == "y":
        cursor.execute("DELETE FROM ingredients WHERE title='%s'" % item)
#Example: query = "delete from zoznam where name = '%s' " % data3
        #sql = '''DELETE FROM ingredients
        #         WHERE title="{item}"'''
    elif confirm.lower() == "n":
        print "Ok, NOT deleting item."
    else:
        "Sorry, that's not valid."
    #try:
        #cursor.execute(sql)
        
    #except:
        #print "Failed to delete item!"

def menu():
    print
    print "What do you want to do?"
    print "A - Add an ingredient"
    print "S - Search for an ingredient"
    print "L - List all ingredients"
    print "U - Update ingredient"
    print "D - Delete ingredient"
    print "Q - Quit"
    choice = raw_input("Choice [A/S/L/U/D/Q]: ")
    return choice[0].lower()

def main():
    conn = open_database("inventory.db")
    cursor = conn.cursor()

    while True:
        choice = menu()
        if choice == "a":
            add_ingredient(cursor)
        elif choice == "s":
            #item = raw_input("What ingredient? ")
            #find_ingredient(cursor, item)
            find_ingredient(cursor)
        elif choice == "l":
            list_ingredients(cursor)
        elif choice == "u":
            update_ingredient(cursor)
        elif choice == "d":
            delete_ingredient(cursor)
        elif choice == "q":
            print "Goodbye..."
            break
        else:
            print "Sorry, that's not valid"

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
    
    
            
        
