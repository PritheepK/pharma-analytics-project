import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize contexts
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# S3 source path
sales_path = "s3://pharma-data-project/raw/sales/drug_sales.csv"

# Read CSV file from S3
sales_df = spark.read.option("header", "true").option("inferSchema", "true").csv(sales_path)

# Basic cleaning steps
cleaned_sales_df = sales_df.dropna()  # Remove rows with nulls
cleaned_sales_df = cleaned_sales_df.dropDuplicates()  # Remove duplicates

# Optional: format date column
from pyspark.sql.functions import to_date
cleaned_sales_df = cleaned_sales_df.withColumn("sale_date", to_date("sale_date", "yyyy-MM-dd"))

# Write cleaned data back to S3 (Parquet format)
output_path = "s3://pharma-data-project/processed/cleaned_sales/"
cleaned_sales_df.write.mode("overwrite").parquet(output_path)

# Complete job
job.commit()
