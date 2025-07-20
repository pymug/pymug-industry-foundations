import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqlatuto/todo.db')

df = pd.read_sql('SELECT * FROM todos', con=engine)

print(df.head())