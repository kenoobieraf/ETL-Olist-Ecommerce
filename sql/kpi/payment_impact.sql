SELECT
    p.payment_type,
    ROUND(AVG(f.order_cycle_time_days), 2) AS avg_delivery_days,
    COUNT(*) AS total_orders
FROM fact_orders f
JOIN dim_payments p
    ON f.order_id = p.order_id
WHERE f.order_cycle_time_days IS NOT NULL
GROUP BY p.payment_type
ORDER BY avg_delivery_days DESC;
