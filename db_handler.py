
import sqlite3

def setup_dummy_database():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE employees (id INTEGER, name TEXT, department TEXT, salary INTEGER)")
    cur.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
        (1, "Alice", "Engineering", 90000),
        (2, "Bob", "HR", 70000),
        (3, "Charlie", "Finance", 80000)
    ])
    conn.commit()
    return conn
