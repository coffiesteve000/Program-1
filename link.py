import sqlite3
class CustomerDB:
	def __init__(self) -> None:
		# create/open database and connect
		with sqlite3.connect('customers.db') as self.connection:
			self.conn = self.connection.cursor()
			# create table if not exist
			self.conn.execute("CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY AUTOINCREMENT, \
				name TEXT, contact TEXT, service TEXT, cost INTEGER, actual_date TEXT)")

	def insert_into_db(self, name, contact, service, cost, actual_date)	-> str:
		try:
			self.conn.execute("INSERT INTO customers (name, contact, service, cost, actual_date) VALUES (?, ?, ?, ?, ?)",(name, contact, service, cost, actual_date))
			self.connection.commit()
			return "Added Successfully"
		except Exception:
			return "Unable to add data"
	def return_all(self) -> list:
		try:
			self.conn.execute("SELECT actual_date, name, contact, service, cost FROM customers")
			self.fetchall = self.conn.fetchall()
			return self.fetchall
		except Exception:
			return "Unable to retrieve data from database"

