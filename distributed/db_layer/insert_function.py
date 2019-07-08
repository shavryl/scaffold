from sqlalchemy import insert
from distributed.db_layer.table_schema import cookies, engine
from pprint import pprint


ins = cookies.insert().values(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://bla.bla/recipe.html',
    cookie_sku='CC01',
    quantity='12',
    unit_cost='0.50'
)

inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    }
]

connection = engine.connect()
result = connection.execute(ins, inventory_list)

pprint(result)
