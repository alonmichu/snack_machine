from database import Database

snack_db = Database('snack_machine')
connection = snack_db.get_connection()
# snack_db.create_table(connection)
# snack_db.set_default_characteristic(connection)
# print(snack_db.get_max_stock(connection))
# snack_db.set_default_snack(connection)
# print(snack_db.get_snacks(connection))
# print(snack_db.buy_snack(connection, 15))
# print(snack_db.get_snacks(connection))
# print(snack_db.add_snack(connection, 15, 5))
# print(snack_db.get_snacks(connection))