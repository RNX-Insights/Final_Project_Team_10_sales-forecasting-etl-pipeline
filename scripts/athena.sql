CREATE TABLE sales_forecasting.final_output_safe
WITH (
  format = 'Parquet',
  external_location = 's3://sales-forecasting-parquet-clean/final/',
  write_compression = 'SNAPPY'
) AS
SELECT
  "order id" AS order_id,
  "order date" AS order_date,
  "region",
  "state",
  CAST("sales" AS DOUBLE) AS sales,
  "sales_category"
FROM sales_forecasting.processed_sales
WHERE "sales" IS NOT NULL;
