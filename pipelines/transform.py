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
        o.order_delivered_carrier_date,
        o.order_estimated_delivery_date,
        o.order_approved_at,

    DATE_DIFF(
        'day',
        o.order_purchase_timestamp,
        o.order_delivered_customer_date
    ) AS order_cycle_time_days,
    
    DATE_DIFF(
        'day',
        o.order_estimated_delivery_date,
        o.order_delivered_customer_date
    ) AS delivery_delay_days

FROM raw_orders o
LEFT JOIN raw_order_items oi
    ON o.order_id = oi.order_id
""")


con.execute("""
CREATE OR REPLACE TABLE dim_sellers AS
SELECT DISTINCT
    seller_id,
    seller_city,
    seller_state
FROM raw_sellers
""")

con.execute("""
CREATE OR REPLACE TABLE dim_products AS
SELECT DISTINCT
    product_id,
    product_category_name,
    product_weight_g
FROM raw_products
""")

con.execute("""
CREATE OR REPLACE TABLE dim_payments AS
SELECT
    order_id,
    payment_type,
    payment_installments,
    payment_value
FROM raw_payments
""")

for table, file in raw_tables.items():
    con.execute(f"""
        CREATE OR REPLACE TABLE {table} AS
        SELECT * FROM read_csv_auto('{RAW_DATA_DIR / file}')
    """)

tables_list = con.sql("SELECT * FROM fact_orders LIMIT 5")
print(tables_list)

con.close()