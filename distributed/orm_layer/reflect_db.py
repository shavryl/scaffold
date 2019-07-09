from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine


Base = automap_base()

engine = create_engine('sqlite:///ormtest.db')

