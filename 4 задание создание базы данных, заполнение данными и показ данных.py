import sqlite3

conn = sqlite3.connect('adjutanted.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    executor TEXT,
    amount INTEGER
)
''')

# Вставка данных
cursor.executemany('''
INSERT INTO orders (customer, executor, amount)
VALUES (?, ?, ?)
''', [
    ('Русинов А.А.', 'Данилов Н.А.', 100000),
    ('Рединов Д.М.', 'Минаева М.Д.', 150000),
    ('Баландин А.В.', 'Давыдов Р.Д.', 70000)
])

conn.commit()

cursor.execute('SELECT * FROM orders')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
