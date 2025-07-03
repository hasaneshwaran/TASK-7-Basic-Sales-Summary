import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

sample_data = [
    ("Laptop", 5, 60000),
    ("Mouse", 15, 500),
    ("Keyboard", 10, 1500),
    ("Monitor", 7, 12000),
    ("Laptop", 3, 62000),
    ("Mouse", 10, 550),
    ("Keyboard", 5, 1600),
    ("Monitor", 2, 12500)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

conn.commit()
conn.close()

print("✅ sales_data.db created with sample data!")
