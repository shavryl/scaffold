from sqlalchemy import create_engine


engine = create_engine('sqlite:///mydb.db')

connection = engine.connect()
