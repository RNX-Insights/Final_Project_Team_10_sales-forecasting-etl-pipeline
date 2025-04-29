import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')

    # 1. Start the crawler
    crawler_name = "sales-raw-crawler"
    glue.start_crawler(Name=crawler_name)
    print(f"Started crawler: {crawler_name}")

    # 2. Start Glue ETL Job
    job_name = "sales-etl-job"
    glue.start_job_run(JobName=job_name)
    print(f"Started job: {job_name}")

    return {
        'statusCode': 200,
        'body': 'Crawler and ETL job started.'
    }
