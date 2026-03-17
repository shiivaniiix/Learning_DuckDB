import duckdb

#duckdb.query("SELECT * FROM 'orders.csv'").show()

con = duckdb.connect("my_database.duckdb")

con.execute("CREATE TABLE orders AS SELECT * FROM 'orders.csv'")
con.execute("SELECT * FROM 'orders.csv'").show()