import duckdb
URL="https://www.sidc.be/cactus/out/cmecat.txt"
db_file='cme_data.db'
con=duckdb.connect(database=db_file,read_only=False)
con.execute("INSTALL httpfs;")
con.execute("LOAD httpfs;")

