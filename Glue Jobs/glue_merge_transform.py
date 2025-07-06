import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, expr, to_date

# Init Glue job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# S3 input paths
sales_path = "s3://pharma-data-project/processed/cleaned_sales/"
inventory_path = "s3://pharma-data-project/processed/cleaned_inventory/"

# Read both cleaned Parquet datasets
df_sales = spark.read.parquet(sales_path)
df_inventory = spark.read.parquet(inventory_path)

# Optional: cast date formats again if needed
df_sales = df_sales.withColumn("sale_date", to_date("sale_date", "yyyy-MM-dd"))
df_inventory = df_inventory.withColumn("last_updated", to_date("last_updated", "yyyy-MM-dd"))

# Join on drug_id
df_joined = df_sales.join(df_inventory, on="drug_id", how="inner")

# Add total revenue column
df_joined = df_joined.withColumn("total_revenue", col("units_sold") * col("price"))

# Save final merged data to S3 (Parquet format)
output_path = "s3://pharma-data-project/processed/sales_inventory_joined/"
df_joined.write.mode("overwrite").parquet(output_path)

# Complete Glue job
job.commit()
