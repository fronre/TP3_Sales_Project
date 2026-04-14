# 📊 Sales Data Analysis Project

## 🚀 Overview

This project presents a complete **end-to-end data analysis pipeline** using **Python** and **Power BI**.

It covers:

* Data cleaning & preprocessing
* Exploratory Data Analysis (EDA)
* Customer segmentation using Machine Learning
* Interactive dashboard visualization

🎯 The goal is to transform raw sales data into **actionable business insights**.

---

## 🧠 Objectives

* 📈 Analyze sales performance over time
* 🥇 Identify top-performing products
* 🌍 Explore sales distribution across countries
* 👥 Segment customers based on behavior
* 📊 Build an interactive Power BI dashboard

---

## 🏗️ Project Structure

```
TP3_Sales_Project/
│
├── data/
│   └── SuperStoreOrders.csv
│
├── output/
│   ├── cleaned_data.csv
│   ├── figure_1_sales_trend.png
│   ├── figure_2_top_products.png
│   ├── figure_3_country_sales.png
│   ├── figure_4_heatmap.png
│   └── figure_5_customer_clusters.png
│
├── src/
│   ├── cleaning.py
│   ├── analysis.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## 📦 Dataset Description

The dataset contains transactional sales records with the following key features:

| Feature     | Description                |
| ----------- | -------------------------- |
| InvoiceDate | Transaction date           |
| CustomerID  | Unique customer identifier |
| Country     | Customer location          |
| Description | Product name               |
| Sales       | Revenue generated          |
| Quantity    | Number of units sold       |

---

## 🧹 Data Cleaning

Performed using **Pandas** in `cleaning.py`.

### Steps:

* ❌ Removed missing values
* 🔁 Removed duplicate records
* 📅 Converted date columns
* 🔢 Ensured numeric consistency

📁 Output:

```
output/cleaned_data.csv
```

---

## 🔎 Exploratory Data Analysis (EDA)

Performed in `analysis.py`.

### 📊 Key Visualizations:

* 📈 **Sales Trend Over Time**
* 🥇 **Top 10 Products**
* 🌍 **Sales by Country**
* 🔗 **Correlation Heatmap**

---

## 🤖 Customer Segmentation

Applied **K-Means Clustering** to group customers based on:

* Total Sales
* Total Quantity

### Segments:

* 🟢 High-value customers
* 🟡 Medium-value customers
* 🔴 Low-value customers

---

## 📊 Power BI Dashboard

An interactive dashboard was created for dynamic data exploration.

🔗 **Access Dashboard:**
https://app.powerbi.com/links/hicPspR_38?ctid=fa7e31a0-d802-442a-a11d-dd99271b08bb

### Features:

* KPI cards (Sales, Quantity, Customers)
* Top products visualization
* Country analysis
* Time-based trends
* Interactive filters (slicers)

---

## 🛠️ Technologies Used

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 📉 Matplotlib
* 🎨 Seaborn
* 🤖 Scikit-learn
* 📊 Power BI

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run the project

```
python src/main.py
```

### 3. Output

* Cleaned dataset → `output/cleaned_data.csv`
* Visualizations → `output/`

---

## 📈 Key Insights

* Certain products dominate total sales
* Sales distribution varies significantly across countries
* A small group of customers contributes most of the revenue
* Customer segmentation helps identify high-value customers

---

## 📌 Future Improvements

* Add real-time data integration
* Enhance dashboard interactivity
* Deploy as a web application
* Use advanced ML models

---

## 👤 Author

**Islam Mohammed**

---

## ⭐ Project Value

This project demonstrates:

* Real-world data analysis workflow
* Integration between Python and Power BI
* Data-driven decision-making

---

## 📬 Contact

Feel free to reach out for collaboration or questions.
