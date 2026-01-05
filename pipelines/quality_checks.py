import duckdb
from pathlib import Path
import sys

DB_PATH = "db/olist.duckdb"
QC_DIR = Path("sql/quality_checks")

con = duckdb.connect(DB_PATH)

failed = False

for qc_file in QC_DIR.glob("*.sql"):
    query = qc_file.read_text()
    df = con.execute(query).fetchdf()

    if not df.empty:
        print(f"Data quality failed: {qc_file.name}")
        print(df.head())
        failed = True
    else:
        print(f"Passed: {qc_file.name}")

con.close()

if failed:
    sys.exit(1)
