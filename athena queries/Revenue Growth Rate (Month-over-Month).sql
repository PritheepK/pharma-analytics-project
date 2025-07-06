WITH monthly_revenue AS (
  SELECT 
    DATE_TRUNC('month', sale_date) AS month,
    SUM(units_sold * price) AS total_revenue
  FROM 
    sales_inventory_joined
  GROUP BY 
    month
),
revenue_with_lag AS (
  SELECT *,
    LAG(total_revenue) OVER (ORDER BY month) AS prev_month_revenue
  FROM monthly_revenue
)
SELECT 
  month,
  total_revenue,
  prev_month_revenue,
  ROUND(
    (total_revenue - prev_month_revenue) / prev_month_revenue * 100, 2
  ) AS growth_rate_percentage
FROM 
  revenue_with_lag
WHERE 
  prev_month_revenue IS NOT NULL;
