SELECT *
FROM fact_orders
WHERE order_status = 'delivered'
  AND order_estimated_delivery_date IS NULL;
