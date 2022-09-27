import dataset

db = dataset.connect("sqlite:///shopping_list.db")

def get_items(id=None):
    table = db['list']
    items = []
    if id:
        item = table.find_one(id=id)
        items.append(dict(item))
    else:
        items = table.find()
        items = [dict(i) for i in items]
    return items


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


if __name__ == "__main__":
    print(get_items(1))



