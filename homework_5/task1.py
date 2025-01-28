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

# SQL-запрос для получения наименований продуктов в диапазоне цен
query = """
SELECT product_name
FROM products
WHERE unit_price >= 3 AND unit_price < 7;
"""

# Выполняем запрос
cursor.execute(query)

# Извлекаем результаты
products = cursor.fetchall()

# Получаем количество затронутых строк
affected_rows = cursor.rowcount

# Формируем данные для вывода
table_data = [(i+1, product[0]) for i, product in enumerate(products)]

# Выводим результаты в виде таблицы
print(tabulate(table_data, headers=["#", "Product Name"], tablefmt="grid"))

# Выводим количество затронутых строк
print(f"Affected rows: {affected_rows}")

# Закрываем курсор и соединение с базой данных
cursor.close()
conn.close()
