import sqlalchemy as db
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Создание движка (engine)
# обязательно наличие уже существующей бд european_database.sqlite в той же папке
engine = db.create_engine("sqlite:///european_database.sqlite")
conn = engine.connect()

# Создание метаданных
metadata = db.MetaData()

# Загрузка таблицы 'divisions'
division = db.Table('divisions', metadata, autoload_with=engine)

# Загрузка таблицы 'matchs'
match = db.Table('matchs', metadata, autoload_with=engine)

# Указание столбцов, которые вы хотите выбрать
columns = (
    division.columns.division,
    match.columns.HomeTeam,
    match.columns.FTHG,
    match.columns.FTAG,
)

# Построение запроса
query = db.select(*columns).select_from(division.join(match, division.columns.division == match.columns.Div)).where(db.and_(division.columns.division == "E1", match.columns.season == 2009)).order_by(match.columns.HomeTeam)

# Выполнение запроса и извлечение результатов
output = conn.execute(query)
results = output.fetchall()

# Создание DataFrame из результатов
data = pd.DataFrame(results, columns=["Division", "HomeTeam", "FTHG", "FTAG"])

# Построение графика с использованием библиотеки seaborn
sns.set_theme(style="whitegrid")
f, ax = plt.subplots(figsize=(15, 6))
plt.xticks(rotation=90)
sns.set_color_codes("pastel")
sns.barplot(x="HomeTeam", y="FTHG", data=data, label="Голы домашней команды", color="b")
sns.barplot(x="HomeTeam", y="FTAG", data=data, label="Голы гостевой команды", color="r")
ax.legend(ncol=2, loc="upper left", frameon=True)
ax.set(ylabel="", xlabel="")
sns.despine(left=True, bottom=True)

# Отображение графика
plt.show()
