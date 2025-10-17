import duckdb
result=duckdb.sql(r"SELECT * FROM read_csv('D:\Python0\industry.csv',delim='|')")
result.show()