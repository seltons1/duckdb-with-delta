import duckdb

conn = duckdb.connect(':memory:') 

try:
    
    query = """SELECT title, location, views FROM delta_scan('raw/jobs') where UPPER(title) like '%DATA ENGINEER%' """

    result = conn.execute(query)

    df = result.fetchdf()
    print(df)

except duckdb.InvalidInputException as e:

    print(f"Erro de entrada inválida: {e}")

except Exception as e:

    print(f"Outro erro ocorreu: {e}")

finally:

    conn.close()