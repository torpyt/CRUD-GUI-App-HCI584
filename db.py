import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                         (part, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# db = Database('store.db')
# db.insert("Sprayer hose", "James Doe", "John Deere Omaha", "2,000")
# db.insert("Brake steering system", "Mike Henry", "John Deere Springfield", "13,000")
# db.insert("Clutch replacement", "Karen Johnson", "John Deere Lincoln", "5,000")
# db.insert("Transmission gears", "Albert Gilbertson", "John Deere Columbia", "2,000")
# db.insert("Torque converter gear", "Sam Smith", "John Deere Des Moines", "2,500")
# db.insert("Compact tractor wheels", "Robert Frost", "John Deere Omaha", "18,000")
# db.insert("Tractor pulley", "Alyssa Edwards", "John Deere Springfield", "20,000")