import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Glue job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define S3 input path for inventory
inventory_path = "s3://pharma-data-project/raw/inventory/inventory.csv"

# Read inventory data
inventory_df = spark.read.option("header", "true").option("inferSchema", "true").csv(inventory_path)

# Basic cleaning
cleaned_inventory_df = inventory_df.dropna()  # Remove nulls
cleaned_inventory_df = cleaned_inventory_df.dropDuplicates()  # Remove duplicates

# Convert last_updated to date format
from pyspark.sql.functions import to_date
cleaned_inventory_df = cleaned_inventory_df.withColumn("last_updated", to_date("last_updated", "yyyy-MM-dd"))

# Write cleaned inventory data to S3 as Parquet
output_path = "s3://pharma-data-project/processed/cleaned_inventory/"
cleaned_inventory_df.write.mode("overwrite").parquet(output_path)

# Complete job
job.commit()
