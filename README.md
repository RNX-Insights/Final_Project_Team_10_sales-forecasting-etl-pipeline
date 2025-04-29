# Final_Project_Team_10_sales-forecasting-etl-pipeline
Automated ETL and Visualization Pipeline using AWS S3, Glue, Athena, Lambda, and Power BI

# Sales Forecasting ETL and Visualization Pipeline

🚀 **Project Summary:**  
This project implements an end-to-end automated ETL and analytics pipeline for sales data, leveraging AWS cloud services (S3, Glue, Lambda, Athena) combined with Power BI for business visualization. The primary goal is to streamline data ingestion, transformation, and visualization processes to support better decision-making and identify operational inefficiencies.

The project follows the **CRISP-DM (Cross-Industry Standard Process for Data Mining)** methodology:
- **Business Understanding:** Improve operational efficiency and optimize sales performance by identifying regional and category-based sales patterns.
- **Data Understanding:** Ingest raw CSV sales data from diverse regions and time periods.
- **Data Preparation:** Clean, transform, and structure the data using AWS Glue ETL jobs.
- **Modeling:** Design automated workflows (Lambda + Glue) for seamless data processing.
- **Evaluation:** Analyze results through detailed Power BI dashboards.
- **Deployment:** Automate the pipeline to process new incoming data with minimal manual intervention.

---

## 📚 Project Architecture

1. 📂 **S3 Raw Data Bucket** — Upload raw CSV sales data
2. 🔁 **AWS Lambda** — Triggered on CSV upload, starts Glue Crawler and ETL job
3. 🔍 **AWS Glue Crawler** — Updates table schema
4. 🔨 **AWS Glue ETL Job** — Cleans and processes data into Parquet format
5. 🎯 **Athena** — Query processed data
6. 📊 **Power BI** — Visualize key business insights

---

## 🛠 Technology Stack

- **AWS S3** — Storage for raw and processed data
- **AWS Glue** — Data cataloging and ETL
- **AWS Lambda** — Event-driven orchestration
- **AWS Athena** — Serverless SQL querying
- **Power BI** — Business intelligence dashboarding
- **Python** — Lambda and Glue scripting

---

## 📁 Repository Structure

```
/data
  /raw           # Sample raw sales CSV
  /processed     
/scripts
  glue_etl_job_script.py
  lambda_trigger_script.py
/docs
  Technical_Report.docx
  Pitch_Deck.pptx
architecture_diagram.png
README.md
```

---

## 📊 Key Visualizations

- Total Sales KPI
- Sales by Region
- Monthly Sales Trend
- Sales Category Distribution
- Geographic Sales Map
- Operational Inefficiencies Insights

---

## 🔮 Future Improvements

- Automatic dashboard refresh using AWS EventBridge
- Add data quality validation before ETL ingestion
- Real-time ingestion and analytics using AWS Kinesis and QuickSight

---
