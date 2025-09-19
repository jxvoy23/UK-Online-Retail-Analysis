# UK Online Retail Analysis

This project analyzes a transactional dataset from a UK-based online retail store. The dataset contains all transactions from **January 12, 2010, to September 12, 2011**. Using Python and pandas, this project computes key business metrics, generates insights on customer behavior, and visualizes revenue trends and top-selling products.

---

## **Project Features**

### 1. Data Analysis
- **Top Products**
  - Identifies the overall top-selling product by quantity.
  - Highlights the top product during the holiday season (December 2010).  
- **Top Countries**
  - Finds the country that purchased the most products.
  - Lists the top 5 countries by total products sold.
  - Computes average daily revenue for the top countries.
  - Calculates total revenue for a specific calendar year (example: 2011).  
- **Revenue & Sales Analysis**
  - Computes total revenue per transaction (`Quantity × UnitPrice`).
  - Calculates average revenue per day across the dataset.

### 2. Visualizations
- Daily revenue trends over time.
- Top 10 products by quantity sold.
- Top 5 countries by revenue.
- Daily revenue trends for the top 5 countries.  

All visualizations are saved as **PNG files** in the `figures/` folder.

### 3. CSV Reports
All computed metrics are saved as **CSV files** in the `csv_reports/` folder for easy reference and sharing:
- Top product overall
- Top holiday product
- Average revenue per day
- Top 5 countries by products sold
- Average daily revenue for top countries
- Total yearly revenue for top countries  

---

## **Getting Started**

### Prerequisites
- Python 3.x
- Packages: `pandas`, `matplotlib`, `seaborn`, `openpyxl`

Install dependencies using pip:

```bash
pip install pandas matplotlib seaborn openpyxl
