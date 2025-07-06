SELECT 
  region,
  warehouse_id,
  SUM(units_sold * price) AS total_revenue
FROM 
  sales_inventory_joined
GROUP BY 
  region, warehouse_id
QUALIFY 
  ROW_NUMBER() OVER (PARTITION BY region ORDER BY SUM(units_sold * price) DESC) = 1;
