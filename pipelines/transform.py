import duckdb
import numpy as np
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")
DB_PATH = "db/olist.duckdb"

con = duckdb.connect(DB_PATH)

raw_tables = {
    "raw_orders": "olist_orders_dataset.csv",
    "raw_customers": "olist_customers_dataset.csv",
    "raw_sellers": "olist_sellers_dataset.csv",
    "raw_order_items": "olist_order_items_dataset.csv",
    "raw_payments": "olist_order_payments_dataset.csv",
    "raw_products": "olist_products_dataset.csv",
}

con.execute("""
    CREATE OR REPLACE TABLE dim_customers AS
    SELECT
        customer_id,
        customer_city,
        customer_state
    FROM raw_customers
""")

con.execute("""
    CREATE OR REPLACE TABLE fact_orders AS
    SELECT
        o.order_id,
        o.customer_id,
        oi.seller_id,
        o.order_status,
        o.order_purchase_timestamp,
        o.order_delivered_customer_date,

        DATE_DIFF(
            'day',
            o.order_purchase_timestamp,
            o.order_delivered_customer_date
        ) AS order_cycle_time_days

    FROM raw_orders o
    LEFT JOIN raw_order_items oi
        ON o.order_id = oi.order_id
""")


for table, file in raw_tables.items():
    con.execute(f"""
        CREATE OR REPLACE TABLE {table} AS
        SELECT * FROM read_csv_auto('{RAW_DATA_DIR / file}')
    """)

tables_list = con.sql("SELECT * FROM fact_orders LIMIT 5")
print(tables_list)

con.close()