import dataset

db = dataset.connect("sqlite:///shopping_list.db")

try:
    db.begin()
    db['list'].drop()
    table = db['list']

    items = [
        {
            "description": "apples"
        },
        {
            "description": "broccoli"
        },
        {
            "description": "pizza"
        },
        {
            "description": "tangerine"
        },
        {
            "description": "potatoes"
        }
        ]

    # inserting one item at a time
    # for item in items:
    #     table.insert(item)


    # inserting multiple items at a time

    table.insert_many(items)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

print("done")