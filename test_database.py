# test_database.py - tests for database functions

# from sql_database import get_items, add_item, update_item, delete_item
from dataset_database import get_items
import time

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
    assert 'description' in items[0].keys()
    assert type(items[0]['id']) is int
    assert type(items[0]['description']) is str
    pass

def test_add_item():
    print("testing add items")
    desc = random_string()
    add_item(desc)
    items = get_items()
    item = items[-1]
    assert desc == item["description"]
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
        assert desc != i["description"]
    pass


def test_update_item():
    print("testing update item")
    desc = random_string()
    add_item(desc)
    items = get_items()
    item = items[-1]
    id, desc = item["id"], item["description"]
    new_desc = desc.replace("1", "9").replace(".", ",")
    update_item(id, new_desc)
    new_items = get_items()
    assert len(items) == len(new_items)
    new_found = False
    for i in new_items:
        if i["id"] == int(id):
            assert new_desc == i["description"]
            new_found = True
        assert i["description"] != desc
    assert new_found


if __name__ == "__main__":
    test_get_items()
    # test_add_item()
    # test_delete_item()
    # test_update_item()
    print("done")






