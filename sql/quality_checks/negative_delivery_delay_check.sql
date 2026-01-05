SELECT *
FROM fact_orders
WHERE delivery_delay_days < -30;
