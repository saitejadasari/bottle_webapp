from bottle import default_app, route, template, get, post, request, redirect
# import sql_database as database
import dataset_database as database

@route('/hello')
def hello_world():
    return 'Hello from the otherside!!'


@route('/')
@route('/list')
def get_list():
    rows = database.get_items()
    return template("shopping_list.tpl", name="Dr. DeLozier", shopping_list=rows)

@get('/add')
def get_add():
    return template('shopping_list.tpl')


@post('/add')
def post_add():
    description = request.forms.get("description")
    quantity = request.forms.get("quantity")
    try:
        quantity = int(quantity)
    except:
        quantity = 1
    database.add_item(description, quantity)
    redirect('/list')

@route('/delete/<id>')
def get_delete(id):
    database.delete_item(id)
    redirect('/list')

@get('/edit/<id>')
def get_edit(id):
    items = database.get_items(id)
    if len(items) != 1:
        redirect('/list')
    else:
        item = items[0]
        item_id, description = item["id"], item["description"]
        return template('edit_item.tpl', id=id, description=description)

@post('/edit/<id>')
def post_edit(id):
    description = request.forms.get("description")
    database.update_item(id, description)
    redirect('/list')


application = default_app()
