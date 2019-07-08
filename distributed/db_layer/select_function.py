from sqlalchemy.sql import select, func
from distributed.db_layer.table_schema import engine, cookies, connection, orders, users, line_items
from pprint import pprint


s = select(
    [cookies.c.cookie_name, cookies.c.quantity, cookies.c.unit_cost]
)
rp = connection.execute(s)
print(rp.keys())
result = rp.first()



ord = s.order_by(cookies.c.quantity)
rr = connection.execute(ord)
for cookie in rr:
    print('{} - {} - {}'.format(cookie.quantity, cookie.cookie_name, cookie.unit_cost))


def get_orders_by_customers(cust_name, shipped=None, details=False):
    columns = [orders.c.order_id, users.c.username, users.c.phone]
    joins = users.join(orders)
    if details:
        columns.extend([cookies.c.cookie_name, line_items.c.quantity,
                        line_items.c.extended_cost])
        joins = joins.join(line_items).join(cookies)
    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(joins)
    cust_orders = cust_orders.where(users.c.username == cust_name)
    if shipped is not None:
        cust_orders = cust_orders.where(orders.c.shipped == shipped)
    result = connection.execute(cust_orders).fetchall()
    return result

