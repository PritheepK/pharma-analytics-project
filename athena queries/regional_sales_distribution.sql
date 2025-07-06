SELECT 
  region,
  drug_id,
  SUM(units_sold) AS total_units_sold
FROM 
  sales_inventory_joined
GROUP BY 
  region, drug_id
ORDER BY 
  region, total_units_sold DESC;
