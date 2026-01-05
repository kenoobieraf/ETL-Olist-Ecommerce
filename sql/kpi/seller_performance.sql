SELECT
    seller_id,
    ROUND(AVG(order_cycle_time_days), 2) AS avg_delivery_days,
    COUNT(*) AS total_orders
FROM fact_orders
WHERE order_cycle_time_days IS NOT NULL
GROUP BY seller_id
ORDER BY avg_delivery_days DESC;
