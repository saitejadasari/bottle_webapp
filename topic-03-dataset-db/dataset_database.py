import dataset

db = dataset.connect("sqlite:///shopping_list.db")

def get_items(id=None):
    table = db['list']
    items = []
    if id:
        item = table.find_one(id=int(id))
        items.append(dict(item))
    else:
        items = table.find()
        items = [dict(i) for i in items]
    return items


def add_item(description, quantity):
    db.begin()
    try:
        table = db['list']
        item = { "description": description, "quantity": int(quantity)}
        table.insert(item)
        db.commit()
        db.close()
    except:
        db.rollback()

def delete_item(id):
    db.begin()
    try:
        table = db['list']
        table.delete(id=int(id))
        db.commit()
        db.close()
    except Exception as ex:
        print(ex)
        db.rollback()

def update_item(id, description):
    db.begin()
    try:
        table = db['list']
        data = dict(id=int(id), description=description)
        table.upsert(data, ['id'])
        db.close()
    except Exception as ex:
        print(ex)
        db.rollback()


# if __name__ == "__main__":
#     print(get_items())
    # add_item("french fries", 10)
    # delete_item(4)



