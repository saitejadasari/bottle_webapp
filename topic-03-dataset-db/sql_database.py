import sqlite3

connection = sqlite3.connect("shopping_list.db")


def get_items(id=None):
    cursor = connection.cursor()
    query = "select id, description from list"
    if id:
        query = f"select id, description from list where id={id}"
    rows = cursor.execute(query)
    rows = list(rows)
    rows = [ {'id':row[0] ,'description':row[1]} for row in rows ]
    return rows

def add_item(description):
    cursor = connection.cursor()
    cursor.execute(f"insert into list (description) values('{description}')")
    connection.commit()

def delete_item(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()

def update_item(id, description):
    cursor = connection.cursor()
    cursor.execute(f"update list set description ='{description}' where id={id}")
    connection.commit()






