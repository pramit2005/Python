import duckdb
con=duckdb.connect(database=":memory:")
query=r"""
    SELECT Hospital_Name,
    Location
    Location_Coordinates,
    District,
    Pincode,
    Telephone
    FROM read_csv_auto("D:\Datasets\hospital_directory.csv")
    WHERE District='Kolkata'
    """
a=con.execute(query).df()
print(a.info())