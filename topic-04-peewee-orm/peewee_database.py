# database.py - functions for managing database

from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('shopping_list.db')

class List(Model):
    description = CharField()
    quantity = IntegerField()

    class Meta:
        database = db

def get_items(id=None):
    if id == None:
        items = List.select()
    else:
        items = List.select().where(List.id == int(id))
    print("items in peewee", items)
    items = [{'id':item.id, 'description':item.description, 'quantity': item.quantity} for item in items]
    return items

def add_item(description, quantity):
    List.create(description=description, quantity=quantity)

def delete_item(id):
    q = List.delete().where(List.id == int(id))
    q.execute()

def update_item(id, description):
    q = List.update({List.description: description}).where(List.id == int(id))
    q.execute()
