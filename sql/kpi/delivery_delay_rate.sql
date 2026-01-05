SELECT
    ROUND(
        SUM(CASE WHEN delivery_delay_days > 1 THEN 1 ELSE 0 END)::FLOAT
        / COUNT(*) * 100,
        2
    ) AS delay_rate_pct
FROM fact_orders
WHERE delivery_delay_days IS NOT NULL;
