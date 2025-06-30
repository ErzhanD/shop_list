CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    quantity INTEGER,
    is_bought INTEGER DEFAULT 0
)
"""

INSERT_ITEM = "INSERT INTO items (name, quantity) VALUES (?, ?)"
GET_ALL = "SELECT * FROM items"
UPDATE_STATUS = "UPDATE items SET is_bought = ? WHERE id = ?"
DELETE_ITEM = "DELETE FROM items WHERE id = ?"