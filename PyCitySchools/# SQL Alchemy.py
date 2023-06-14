# SQL Alchemy
from sqlalchemy import create_engine

database_path = Path"../Resources/icecreamstore.sqlite"
# Create Engine
engine = create_engine(f"sqlite:///{database_path}")
# Query All Records in the the Database
data = engine.execute("SELECT * FROM icecreamstore;")
for record in data:
    print(record)
# Query Using a Filter
data = engine.execute("SELECT * FROM icecreamstore WHERE Price > 2.0;")
for record in data:
    print(record)
