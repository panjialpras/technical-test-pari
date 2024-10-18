import sqlite3 as sql

def connect_db():
    return sql.connect('database.db')

def get_all_categories():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM categories')
    rows = cur.fetchall()
    conn.close()
    return rows

def get_all_items():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM item')
    rows = cur.fetchall()
    conn.close()
    return rows

def get_item(item_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM item WHERE id = ?', (item_id,))
    row = cur.fetchone()
    conn.close()
    return row

def create_category(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO categories (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def create_item(category_id, name, description, price):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO item (category_id, name, description, price) VALUES (?, ?, ?, ?)', (category_id, name, description, price))
    conn.commit()
    conn.close()

def update_item(item_id, name, description, price):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('UPDATE item SET name = ?, description = ?, price = ? WHERE id = ?', (name, description, price, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM item WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
