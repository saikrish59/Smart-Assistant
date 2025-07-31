import sqlite3

def setup_dummy_database():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    
    # Use AUTOINCREMENT for ID
    cur.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        department TEXT,
        salary INTEGER
    )
    """)
    
    # Insert without specifying ID
    cur.executemany("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", [
        ("Alice", "Engineering", 90000),
        ("Bob", "HR", 70000),
        ("Charlie", "Finance", 80000)
    ])
    
    conn.commit()
    return conn
