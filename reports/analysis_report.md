# TP03 – Full Data Analysis Project
## Sales Data Analysis using Python & Power BI

---

## 1. Project Objective

The objective of this project is to analyze sales data in order to identify:

- Sales trends over time
- Top-performing products
- Regional sales performance
- Relationships between key business variables

The final deliverable includes data processing using Python and a dashboard built using Power BI.

---

## 2. Data Source

The dataset used is SuperStore Sales Dataset, which contains transactional sales records including:

- Order Date
- Ship Date
- Product Name
- Category and Sub-category
- Region and Country
- Sales
- Profit
- Quantity
- Discount
- Shipping Cost

The dataset was loaded from a CSV file and processed using Python.

---

## 3. Data Cleaning and Preprocessing

The following steps were performed:

- Removed duplicate records
- Converted date columns to datetime format
- Converted numerical columns (sales, profit, quantity, discount, shipping_cost) to numeric format
- Removed rows with missing values
- Saved cleaned dataset for further analysis

This ensured the dataset was consistent and ready for analysis.

---

## 4. Exploratory Data Analysis (EDA)

### 4.1 Sales Over Time

The sales trend from 2011 to 2014 shows:

- A general increasing trend over the years
- 2014 recorded the highest peaks in sales
- Sales show variability, indicating possible seasonal demand patterns

Insight:
Sales performance improved over time, suggesting business growth.

---

### 4.2 Top 10 Products by Sales

The analysis identified the top 10 products generating the highest revenue.

Insight:
A small group of products contributes significantly to total sales, indicating product concentration.

This suggests the company should prioritize marketing and inventory management for these products.

---

### 4.3 Sales by Region

Regional analysis showed:

- Central region has the highest total sales
- South and North regions also perform strongly
- Canada has the lowest sales

Insight:
The company may consider improving strategy in underperforming regions.

---

### 4.4 Correlation Analysis

The correlation matrix revealed:

- Strong positive correlation between Sales and Shipping Cost (0.77)
- Moderate negative correlation between Discount and Profit (-0.47)

Insights:

- Higher discounts reduce profitability.
- Higher sales generally imply higher shipping costs.

This suggests discount strategies must be carefully managed.

---

## 5. Power BI Dashboard

The cleaned dataset was imported into Power BI to create an interactive dashboard including:

- KPI Cards (Total Sales, Total Profit, Average Sales)
- Sales trend line chart
- Top 10 products bar chart
- Sales by region visualization
- Filters for year, region, and category

The dashboard allows interactive exploration of the data and supports business decision-making.

---

## 6. Conclusion

The analysis revealed:

- Continuous sales growth over time
- Strong regional performance differences
- Product revenue concentration
- Negative impact of excessive discounts on profit

Recommendations:

- Focus on high-performing products
- Optimize discount policies
- Strengthen marketing in low-performing regions

This project demonstrates how combining Python for data processing and Power BI for visualization creates a complete end-to-end data analysis solution.