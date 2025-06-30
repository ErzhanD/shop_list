import sqlite3
from db import queries
from config import db_path

def connect():
    return sqlite3.connect("shopping.db")

def init_db():
    conn = connect()
    c = conn.cursor()
    c.execute(queries.CREATE_TABLE)
    conn.commit()
    conn.close()

def add_item(name, quantity):
    conn = connect()
    c = conn.cursor()
    c.execute(queries.INSERT_ITEM, (name, quantity))
    conn.commit()
    conn.close()

def get_items():
    conn = connect()
    c = conn.cursor()
    c.execute(queries.GET_ALL)
    items = c.fetchall()
    conn.close()
    return items

def update_status(item_id, status):
    conn = connect()
    c = conn.cursor()
    c.execute(queries.UPDATE_STATUS, (status, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = connect()
    c = conn.cursor()
    c.execute(queries.DELETE_ITEM, (item_id,))
    conn.commit()
    conn.close()