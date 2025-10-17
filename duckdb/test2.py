import duckdb
import pandas as pd
file_path=r"C:\Users\Pramit\Downloads\cmecat.txt"
rel=duckdb.read_text(file_path)
pd_df=pd.DataFrame(rel)
duckdb.sql('SELECT * FROM pd_df')