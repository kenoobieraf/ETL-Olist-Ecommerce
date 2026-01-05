SELECT
    ROUND(AVG(order_cycle_time_days), 2) AS avg_order_cycle_days
FROM fact_orders
WHERE order_cycle_time_days IS NOT NULL;
