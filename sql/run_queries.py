import duckdb
import sys
from pathlib import Path

DB_PATH = "db/olist.duckdb"

if len(sys.argv) < 2:
    print("Usage: python sql/run_queries.py <path_to_sql_file>")
    sys.exit(1)

sql_file = sys.argv[1]

con = duckdb.connect(DB_PATH)

query = Path(sql_file).read_text()
result = con.execute(query).fetchdf()

print(result)

con.close()
