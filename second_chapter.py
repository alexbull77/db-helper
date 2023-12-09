import sqlalchemy as db
import pandas as pd

# Создание движка (engine)
engine = db.create_engine('sqlite:///my_db')

# Создание соединения (необходимо для выполнения запросов)
connection = engine.connect()

# Создание метаданных для создания таблиц
meta = db.MetaData()

# Создание таблицы 'sports'
sports_table = db.Table(
   'sports', meta, 
   db.Column('id', db.Integer, primary_key=True), 
   db.Column('name', db.String), 
   db.Column('category', db.String), 
   db.Column('players', db.Integer),
)

meta.create_all(engine)

# заполнение таблицы кортежами
sports_data = [
    {'name': 'Football', 'category': 'Team Sport', 'players': 11},
    {'name': 'Basketball', 'category': 'Team Sport', 'players': 5},
    {'name': 'Tennis', 'category': 'Individual Sport', 'players': 1},
    {'name': 'Golf', 'category': 'Individual Sport', 'players': 1},
    {'name': 'Baseball', 'category': 'Team Sport', 'players': 9},
    {'name': 'Swimming', 'category': 'Individual Sport', 'players': 1},
    {'name': 'Volleyball', 'category': 'Team Sport', 'players': 6},
    {'name': 'Soccer', 'category': 'Team Sport', 'players': 11},
    {'name': 'Table Tennis', 'category': 'Individual Sport', 'players': 1},
    {'name': 'Hockey', 'category': 'Team Sport', 'players': 11},
]

connection.execute(db.insert(sports_table), sports_data)

# Выполнение запроса SELECT к таблице 'sports'
query = sports_table.select()
result = connection.execute(query).fetchall()

# Отображение данных с использованием сторонней библиотеки pandas
data = pd.DataFrame(result)
print(data)
