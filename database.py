import sqlite3
import time

connection = sqlite3.connect("shopping_list.db")


def get_items(id=None):
    cursor = connection.cursor()
    query = "select id, description from list"
    if id:
        query = f"select id, description from list where id={id}"
    rows = cursor.execute(query)
    rows = list(rows)
    rows = [ {'id':row[0] ,'desc':row[1]} for row in rows ]
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


# Test Cases
def random_string():
    return str(time.time())

def test_get_items():
    print("testing get items")
    items = get_items()
    assert type(items) is list
    assert len(items) > 0
    assert type(items[0]) is dict
    assert 'id' in items[0].keys()
    assert 'desc' in items[0].keys()
    assert type(items[0]['id']) is int
    assert type(items[0]['desc']) is str
    pass

def test_add_item():
    print("testing add items")
    desc = random_string()
    add_item(desc)
    items = get_items()
    item = items[-1]
    assert desc == item["desc"]
    pass

def test_delete_item():
    print("testing delete items")
    desc = random_string()
    add_item(desc)
    items = get_items()
    item = items[-1]
    id = item["id"]
    delete_item(id)
    new_items = get_items()
    assert len(items) > len(new_items)
    for i in new_items:
        assert desc != i["desc"]
    pass


def test_update_item():
    print("testing update item")
    desc = random_string()
    add_item(desc)
    items = get_items()
    item = items[-1]
    id, desc = item["id"], item["desc"]
    new_desc = desc.replace("1", "9").replace(".", ",")
    update_item(id, new_desc)
    new_items = get_items()
    assert len(items) == len(new_items)
    new_found = False
    for i in new_items:
        if i["id"] == int(id):
            assert new_desc == i["desc"]
            new_found = True
        assert i["desc"] != desc
    assert new_found


if __name__ == "__main__":
    test_get_items()
    test_add_item()
    test_delete_item()
    test_update_item()
    print("done")






