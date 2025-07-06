WITH top_drugs AS (
  SELECT drug_id
  FROM sales_inventory_joined
  GROUP BY drug_id
  ORDER BY SUM(units_sold) DESC
  LIMIT 5
)

SELECT 
  DATE_TRUNC('month', sale_date) AS month,
  drug_id,
  SUM(units_sold) AS total_units_sold,
  SUM(units_sold * price) AS total_revenue
FROM 
  sales_inventory_joined
WHERE 
  drug_id IN (SELECT drug_id FROM top_drugs)
GROUP BY 
  month, drug_id
ORDER BY 
  month, drug_id;
