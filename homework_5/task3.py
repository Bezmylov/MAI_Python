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

# SQL-запрос для получения id поставщика и максимальной цены продукта
query = """
SELECT supplier_id, MAX(unit_price) AS max_price
FROM products
WHERE supplier_id IN (1, 3, 5)
GROUP BY supplier_id
ORDER BY supplier_id;
"""

# Выполняем запрос
cursor.execute(query)

# Извлекаем результаты
suppliers_max_price = cursor.fetchall()

# Получаем количество затронутых строк
affected_rows = cursor.rowcount

# Формируем данные для вывода в таблицу
table_data = [(supplier_id, max_price) for supplier_id, max_price in suppliers_max_price]

# Выводим результат в виде таблицы
print(tabulate(table_data, headers=["Supplier ID", "Max Price"], tablefmt="grid"))

# Выводим количество затронутых строк
print(f"Affected rows: {affected_rows}")

# Закрываем курсор и соединение с базой данных
cursor.close()
conn.close()
