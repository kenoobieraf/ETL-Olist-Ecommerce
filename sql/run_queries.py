import duckdb

DB_PATH = "db/olist.duckdb"

con = duckdb.connect(DB_PATH)

query = """
SELECT
    order_status,
    COUNT(*) AS total_orders,
    AVG(order_cycle_time_days) AS avg_cycle_time_days
FROM fact_orders
GROUP BY order_status
ORDER BY total_orders DESC
"""

result = con.execute(query).fetchdf()
print(result)

con.close()
