from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

output_pdf = 'Sales_Data_Project_Portfolio.pdf'
fig_dir = 'output/figures'
figs = [
    'figure_1_sales_trend.png',
    'figure_2_top_products.png',
    'figure_3_country_sales.png',
    'figure_4_heatmap.png',
    'figure_5_customer_clusters.png'
]

c = canvas.Canvas(output_pdf, pagesize=letter)
width, height = letter

# Page 1: Cover and Overview
c.setFont('Helvetica-Bold', 26)
c.drawCentredString(width / 2, height - 80, 'Sales Data Analysis Project')

c.setFont('Helvetica', 12)
c.drawString(60, height - 120, 'Author: Hala Mohammed islam')
c.drawString(60, height - 140, 'Repository: TP3_Sales_Project')
c.drawString(60, height - 160, 'Data source: data/SuperStoreOrders.csv')

overview_lines = [
    'Project Summary:',
    'This project performs a complete analytics workflow for sales data using Python.',
    'It includes data cleaning, descriptive exploration, and customer segmentation.',
    '',
    'Goals:',
    '- Understand product sales performance.',
    '- Reveal country-level sales distribution.',
    '- Identify customer segments based on purchase behavior.',
    '',
    'Pipeline Steps:',
    '1. Clean raw sales data and standardize formats.',
    '2. Generate descriptive visualizations and statistics.',
    '3. Apply K-Means clustering to segment customers.',
]

y = height - 200
for line in overview_lines:
    c.drawString(60, y, line)
    y -= 16

c.showPage()

# Page 2: Dataset and cleaning details
c.setFont('Helvetica-Bold', 18)
c.drawString(60, height - 70, 'Dataset Description and Cleaning')

dataset_lines = [
    'The dataset contains sales transactions with real-world data quality issues.',
    'Key fields used in this analysis:',
    '- order_date: transaction date.',
    '- customer_name: customer identifier.',
    '- product_name: product description.',
    '- country: country of sale.',
    '- sales: amount sold.',
    '- quantity: number of items sold.',
    '',
    'Cleaning process applied in src/cleaning.py:',
    '1. Read raw CSV using pandas with ISO-8859-1 encoding.',
    '2. Drop duplicate rows to avoid duplicate sales counts.',
    '3. Convert order_date to datetime and remove invalid dates.',
    '4. Remove rows missing customer_name or with zero/negative quantity.',
    '5. Ensure sales and quantity are numeric values using pd.to_numeric.',
    '6. Create standard columns: Sales, Quantity, Description, Country, CustomerID.',
    '7. Extract Year and Month from InvoiceDate for time analysis.',
    '8. Save cleaned data to output/cleaned_data.csv.',
]

y = height - 110
for line in dataset_lines:
    c.drawString(60, y, line)
    y -= 16

c.showPage()

# Page 3: EDA details and first figures
c.setFont('Helvetica-Bold', 18)
c.drawString(60, height - 70, 'Exploratory Data Analysis (EDA)')

eda_lines = [
    'Exploratory analysis is performed in src/analysis.py.',
    'This script generates descriptive figures and statistics to understand key patterns.',
    '',
    'Figure 1: Sales Trend Over Time',
    '- Aggregates sales by transaction date.',
    '- Helps identify seasonality and trends.',
    '',
    'Figure 2: Top 10 Products by Sales',
    '- Ranks products by total revenue.',
    '- Reveals best-selling items.',
]

y = height - 110
for line in eda_lines:
    c.drawString(60, y, line)
    y -= 16

x, y = 60, 180
for fig in figs[:2]:
    path = os.path.join(fig_dir, fig)
    if os.path.exists(path):
        img = ImageReader(path)
        c.drawImage(img, x, y, width=240, height=160, preserveAspectRatio=True, anchor='sw')
    x += 260

c.showPage()

# Page 4: More EDA and correlation
c.setFont('Helvetica-Bold', 18)
c.drawString(60, height - 70, 'Country Sales and Correlation Analysis')

analysis_lines = [
    'Figure 3: Sales by Country',
    '- Compares total revenue across countries.',
    '- Shows which markets produce the highest sales.',
    '',
    'Figure 4: Correlation Heatmap',
    '- Computes correlation matrix for numeric columns.',
    '- Highlights relationships between sales, quantity, discount, profit, and date features.',
    '',
    'These analyses support data-driven decisions such as product focus and regional strategy.',
]

y = height - 110
for line in analysis_lines:
    c.drawString(60, y, line)
    y -= 16

x, y = 60, 240
for fig in figs[2:4]:
    path = os.path.join(fig_dir, fig)
    if os.path.exists(path):
        img = ImageReader(path)
        c.drawImage(img, x, y, width=240, height=180, preserveAspectRatio=True, anchor='sw')
    x += 260

c.showPage()

# Page 5: Customer segmentation
c.setFont('Helvetica-Bold', 18)
c.drawString(60, height - 70, 'Customer Segmentation Details')

segmentation_lines = [
    'Segmentation is handled in src/analysis.py using K-Means clustering.',
    'Customers are grouped by total sales and total quantity purchased.',
    '',
    'Clustering steps:',
    '1. Aggregate sales and quantity at the customer level.',
    '2. Fit KMeans with 3 clusters (random_state=42 for reproducibility).',
    '3. Assign each customer to a cluster.',
    '',
    'Business value:',
    '- Identify high-value customers for retention.',
    '- Spot medium-value groups for upselling.',
    '- Recognize low-value segments for targeted campaigns.',
]

y = height - 110
for line in segmentation_lines:
    c.drawString(60, y, line)
    y -= 16

path = os.path.join(fig_dir, figs[4])
if os.path.exists(path):
    img = ImageReader(path)
    c.drawImage(img, 60, 220, width=460, height=340, preserveAspectRatio=True, anchor='sw')

c.showPage()

# Page 6: Technologies and instructions
c.setFont('Helvetica-Bold', 18)
c.drawString(60, height - 70, 'Tools and Running Instructions')

tools_lines = [
    'The project uses the following technologies:',
    '- Python',
    '- Pandas',
    '- NumPy',
    '- Matplotlib',
    '- Seaborn',
    '- Scikit-learn',
    '- ReportLab (for this PDF generation)',
    '',
    'How to run:',
    '1. Install dependencies with pip install -r requirements.txt',
    '2. Execute python src/main.py to generate cleaned data and figures.',
    '3. Open the generated PDF Sales_Data_Project_Portfolio.pdf for the report.',
]

y = height - 110
for line in tools_lines:
    c.drawString(60, y, line)
    y -= 16

c.save()
print('Created', output_pdf)
