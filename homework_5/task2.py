import psycopg2
from tabulate import tabulate

# Параметры подключения к базе данных PostgreSQL
conn = psycopg2.connect(
    host="95.163.241.236",       # Адрес сервера базы данных
    database="nordwind",     # Имя базы данных
    user="student",       # Имя пользователя
    password="qweasd963" # Пароль пользователя
)

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# SQL-запрос для получения самой низкой цены в категории 1
query = """
SELECT MIN(unit_price) AS min_price
FROM products
WHERE category_id = 1;
"""

# Выполняем запрос
cursor.execute(query)

# Извлекаем результат
min_price = cursor.fetchone()

# Получаем количество затронутых строк
affected_rows = cursor.rowcount

# Формируем данные для вывода
table_data = [(1, min_price[0])]

# Выводим результат в виде таблицы
print(tabulate(table_data, headers=["#", "Min Price"], tablefmt="grid"))

# Выводим количество затронутых строк
print(f"Affected rows: {affected_rows}")

# Закрываем курсор и соединение с базой данных
cursor.close()
conn.close()
