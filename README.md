# Task 7 – Basic Sales Summary using SQLite and Python

## Objective

This task connects a SQLite database to Python, runs SQL queries to summarise total quantity and revenue by product, and displays results using pandas and matplotlib.

---

## Tools Used

- Python
- sqlite3 (built-in)
- pandas
- matplotlib

---

## Files and Code

### 1. create_sales_db.py

Creates `sales_data.db` with a sample `sales` table and data.

```python
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

print("sales_data.db created with sample data!")
