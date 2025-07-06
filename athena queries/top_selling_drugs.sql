SELECT 
  drug_id, 
  SUM(units_sold) AS total_units_sold,
  SUM(units_sold * price) AS total_revenue
FROM 
  sales_inventory_joined
GROUP BY 
  drug_id
ORDER BY 
  total_units_sold DESC
LIMIT 10;
