import duckdb

duckdb.query("""
COPY (SELECT * FROM 'orders.csv') 
TO 'orders.parquet' (FORMAT PARQUET);
""")