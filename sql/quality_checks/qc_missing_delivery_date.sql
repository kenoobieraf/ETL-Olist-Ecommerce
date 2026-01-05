SELECT *
FROM fact_orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NULL;
