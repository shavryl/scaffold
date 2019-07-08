from sqlalchemy.sql import select, func, insert, update
from distributed.db_layer.table_schema import engine, cookies, connection, orders, users, line_items
from pprint import pprint


ins = insert(orders).values(user_id=1, order_id='1')
result = connection.execute(ins)
ins = insert(line_items)
order_items = [
    {
        'order_id': 1,
        'cookie_id': 1,
        'quantity': 9,
        'extended_cost': 4.50
    }
]

result = connection.execute(ins, order_items)

ins = insert(orders).values(user_id=1, order_id='2')
result = connection.execute(ins)
ins = insert(line_items)
order_items = [
    {
        'order_id': 2,
        'cookie_id': 1,
        'quantity': 4,
        'extended_cost': 1.50
    },
    {
        'order_id': 2,
        'cookie_id': 2,
        'quantity': 1,
        'extended_cost': 4.50
    }
]

result = connection.execute(ins, order_items)
