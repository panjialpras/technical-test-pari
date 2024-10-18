import sqlite3 as sql

def connect_db():
    return sql.connect('database.db')

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')

    conn.commit()
    conn.close()

# Initialize tables
create_tables()
