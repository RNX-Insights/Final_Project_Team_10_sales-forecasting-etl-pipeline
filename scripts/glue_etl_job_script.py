import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame  
from pyspark.sql.functions import col, when    

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load from Glue Data Catalog
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database = "sales_forecasting",         
    table_name = "sales_forecasting_raw_1",               
    transformation_ctx = "datasource0"
)

# Convert to DataFrame
df = datasource0.toDF()

# Drop null rows in key fields
df = df.na.drop(subset=["Sales", "Order ID", "Product ID"])

# Convert sales to float
df = df.withColumn("Sales", col("Sales").cast("float"))

# Add new feature: Sales Category
df = df.withColumn("Sales_Category", 
                   when(col("Sales") > 1000, "High")
                   .when(col("Sales") > 100, "Medium")
                   .otherwise("Low"))

# Convert back to DynamicFrame
cleaned_dyf = DynamicFrame.fromDF(df, glueContext, "cleaned_dyf")

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame = cleaned_dyf,
    connection_type = "s3",
    connection_options = {"path": "s3://sales-forecasting-processed-1/"},
    format = "csv",
    transformation_ctx = "datasink"
)

job.commit()
