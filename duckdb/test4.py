import duckdb
con=duckdb.connect('a.txt')
con.execute("CREATE TABLE IF NOT EXISTS txt_test(i INTEGER)")
con.table('txt_test').show()