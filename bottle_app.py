from bottle import default_app, route, template, get, post, request, redirect
import sys

import dataset_database as database


def topic_finder(topic):
    if topic == 1 or topic == 2:
        sys.path.append('/home/saitejad/kent/adv_dbs/data_webapp/bottle_webapp/topic-02-db-abstraction')
        print("path is ", sys.path)
        import database as database
        return database
    elif topic == 3:
        sys.path.append('/home/saitejad/kent/adv_dbs/data_webapp/bottle_webapp/topic-03-dataset-db')
        print("path is ", sys.path)
        import dataset_database as database
        return database
    elif topic == 4:
        sys.path.append('/home/saitejad/kent/adv_dbs/data_webapp/bottle_webapp/topic-04-peewee-orm')
        print("path is ", sys.path)
        import peewee_database as database
        return database


@route('/hello')
def hello_world():
    return 'Hello from the otherside!!'

@route('/')
@route('/list')
def get_list():
    rows = database.get_items()
    return template("shopping_list.tpl", name="Sai teja", shopping_list=rows, topic=2)

@get('/<topic>/list')
def get_list(topic):
    topic = topic if topic else 2
    db = topic_finder(int(topic))
    rows = db.get_items()
    print("Topic ", topic)
    return template("shopping_list.tpl", name="Sai Teja", shopping_list=rows, topic=topic)

@get('/add')
def get_add():
    return template('shopping_list.tpl')


@post('/<topic>/add')
def post_add(topic):
    description = request.forms.get("description")
    quantity = request.forms.get("quantity")
    try:
        quantity = int(quantity)
    except:
        quantity = 1
    topic = topic if topic else 2
    db = topic_finder(int(topic))
    db.add_item(description, quantity)
    redirect('/'+ topic +'/list')

@route('/delete/<topic>/<id>')
def get_delete(topic, id):
    topic = topic if topic else 2
    db = topic_finder(int(topic))
    db.delete_item(id)
    redirect('/'+ topic +'/list')

@get('/edit/<topic>/<id>')
def get_edit(topic, id):
    topic = topic if topic else 2
    db = topic_finder(int(topic))
    items = db.get_items(id)
    if len(items) != 1:
        redirect('/'+ topic +'/list')
    else:
        item = items[0]
        item_id, description = item["id"], item["description"]
        return template('edit_item.tpl', id=id, description=description, topic=topic)

@post('/edit/<topic>/<id>')
def post_edit(topic, id):
    description = request.forms.get("description")
    topic = topic if topic else 2
    db = topic_finder(int(topic))
    db.update_item(id, description)
    redirect('/'+ topic +'/list')


@route('/<topic>/redirect')
def redirect_link(topic):
    redirect('/'+ topic + '/list')

application = default_app()
