Pharmaceutical Drug Sales & Inventory Analytics

A complete end-to-end AWS Data Engineering Project to analyze drug sales, monitor inventory, and visualize supply chain performance---

## Project Objective

Analyze pharmaceutical sales trends, warehouse stock levels, regional distribution, and performance using scalable AWS services and visualization tools.

## Tech Stack

| Tool/Service      | Purpose                                                   |
| ----------------- | --------------------------------------------------------- |
| Amazon S3         | Store raw & processed data files (CSV/Parquet)            |
| AWS Glue          | Data transformation, joining, and cleaning (PySpark jobs) |
| AWS Athena        | Serverless querying using SQL over S3 data                |
| Amazon QuickSight | Dashboards & visualizations                               |
| AWS CloudWatch    | Set up low-stock alert monitoring                         |
| Pandas + Python   | Generate synthetic data locally                           |

---

## Dataset

Synthetic dataset generated using Pandas (100,000 rows)
* `drug_sales.csv`: Includes drug\_id, warehouse\_id, region, units\_sold, price, sale\_date
* `inventory_data.csv`: Includes drug\_id, warehouse\_id, stock\_level

---

##  Data Pipeline Workflow

1. **Generate synthetic data** with Python (drug\_sales + inventory)
2. **Upload to S3**:

   * Raw sales: `s3://pharma-data-project/raw/sales/drug_sales.csv`
   * Raw inventory: `s3://pharma-data-project/raw/inventory/inventory_data.csv`
3. **Glue jobs**:

   * Clean both datasets using `glue_sales_cleaning.py` and `glue_inventory_cleaning.py`
   * Merge and transform data using `glue_merge_transform.py`
   * Save output as `.parquet` to: `s3://pharma-data-project/processed/sales_inventory_joined/data.parquet`
4. **Athena**:

   * Create external tables pointing to S3 files
   * Query data for insights
5. **QuickSight Dashboards**:

   * Connect to Athena
   * Create charts for sales, stock, and regional insights
6. **CloudWatch**:

   * Set alerts when stock level drops below 100
   * JSON config: `cloudwatch/low_stock_alert.json`
