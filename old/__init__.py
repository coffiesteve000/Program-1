import sqlite3

class CustomerDb:
    def __init__(self) -> None:
        # open and connect database as applications starts
        with sqlite3.connect('customers.db') as self.connection:
            self.conn = self.connection.cursor()
            # create initial tables if they dont exist
            self.conn.execute("CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                name TEXT, contact TEXT, service TEXT, cost INTEGER, actual_date TEXT)")
    
    def insert_data_to_database(self, name, contact, service, cost, actual_date) -> str:
        """This method accepts data from the UI and save it to the database

        Args:
            name (str): The customer name
            contact (int): The customer contact number
            service (str): The service details to render to customer
            cost (int): The cost of service
            actual_date (str): The date of service

        Returns:
            Response: Success or failure to insert data 
        """
        try:
            self.conn.execute("INSERT INTO customers (name, contact, service, cost, actual_date) VALUES(?, ?, ?, ?, ?) ", (name, contact, service, cost, actual_date))
            self.connection.commit()
            return "added successfully"
        except Exception:
            return "unable to insert data"

    def delete_data(self, item_id) -> str:
        """This method delete a single item

        Args:
            item_id (Int): Item Id

        Returns:
            Response: Success or unsuccessfull
        """
        try:
            self.conn.execute("DELETE FROM customers WHERE id =?",(item_id))
            self.connection.commit()
            return "Item deleted"
        except Exception:
            return "Sorry could not delete item"
    
    def delete_all_data(self) ->str:
        """Delete all data from customer database

        Returns:
            Responses: Success or unsuccessful
        """
        try:
            self.conn.execute("DELETE FROM customers")
            self.connection.commit()
            return "All Items deleted"
        except Exception:
            return "Sorry could not delete all items. Try again"
    
    def update_data(self,name, contact, service, cost, actual_date, item_id) ->str:
        """Update database base on customer data change. Update a single item

        Args:
            name (str): The customer name
            contact (int): The customer contact number
            service (str): The service details to render to customer
            cost (int): The cost of service
            actual_date (str): The date of service
            item_id (Int): Id of item

        Returns:
            Response: Success or Unsuccessful
        """
        try:
            self.conn.execute("UPDATE customers SET name= ?, contact= ?, service= ?, cost= ?, actual_date= ? WHERE id =?",(name, contact, service, cost, actual_date, Item_id))
            self.connection.commit()
            return "Item Updated"
        except Exception:
            return "Sorry could not update customer items. Try again"

    def return_all_data(self) ->list:
        """Return all data from database to UI table

        Returns:
            list: List of all availabe data from database
        """
        try:
            self.conn.execute("SELECT actual_date, name, contact, service, cost FROM customers")
            self.fetchall = self.conn.fetchall()
            return self.fetchall
        except Exception:
            return "Sorry could not retrieve data from database"


