SELECT
    c.customer_state,
    ROUND(AVG(f.order_cycle_time_days), 2) AS avg_delivery_days,
    COUNT(*) AS total_orders
FROM fact_orders f
JOIN dim_customers c
    ON f.customer_id = c.customer_id
WHERE f.order_cycle_time_days IS NOT NULL
GROUP BY c.customer_state
ORDER BY avg_delivery_days DESC;
