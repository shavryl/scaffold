from sqlalchemy.sql import select, func
from distributed.db_layer.table_schema import engine, cookies, connection
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

