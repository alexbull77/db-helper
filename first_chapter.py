import sqlalchemy as db

# создание движка (engine)
engine = db.create_engine('sqlite:///my_db')

# создание соединения (необходимо для выполнения запросов)
connection = engine.connect()

# создание метаданных (для создания таблиц)
meta = db.MetaData()

# создание таблицы
students_table = db.Table(
   'students', meta, 
   db.Column('id', db.Integer, primary_key = True), 
   db.Column('name', db.String), 
   db.Column('lastname', db.String), 
)

meta.create_all(engine)

# выполнение запроса (в результате получим пустой массив, потому что данных в нашей базе нет)
exe = connection.execute(students_table.select())
result = exe.fetchall()
print(result)

# заплняем таблицу первым кортежем
my_students = [
    (1, 'Ion', 'Ceban')
]
connection.execute(students_table.insert().values(my_students))

# выполнение запроса (в результате получим массив с 1 элементом)
exe = connection.execute(students_table.select())
result = exe.fetchall()
print(result)

# заполняем таблицу еще двумя кортежами (другим методом)
insert_query = db.insert(students_table)

values = [
    {'id': 2, 'name': 'Andrew', 'lastname': 'Ewbanks'},
    {'id': 3, 'name': 'John', 'lastname': 'Travolta'}
]

connection.execute(insert_query, values)

# выполнение запроса (в результате получим массив из 3 кортежей)
exe = connection.execute(students_table.select())
result = exe.fetchall()
print(result)
