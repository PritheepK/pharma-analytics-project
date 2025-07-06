SELECT 
  drug_id,
  warehouse_id,
  stock_level
FROM 
  sales_inventory_joined
WHERE 
  stock_level < 100
ORDER BY 
  stock_level ASC;
