import duckdb
con=duckdb.connect('a.db')
con.execute("CREATE TABLE test( name CHAR,age INTEGER)")
con.execute("INSERT INTO test VALUES('Pramit',20)")
con.table("test").show()
con.close()