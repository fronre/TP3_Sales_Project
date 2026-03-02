import matplotlib.pyplot as plt
import seaborn as sns


def run_analysis(data):
    """
    Perform Exploratory Data Analysis (EDA)
    - Descriptive statistics
    - Sales trends
    - Top products
    - Sales by region
    - Correlation heatmap
    """

    print("\n===== Descriptive Statistics =====")
    print(data.describe())

    # Sales over time
    sales_over_time = data.groupby("order_date")["sales"].sum()

    plt.figure()
    sales_over_time.plot()
    plt.title("Sales Over Time")
    plt.xlabel("Order Date")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Top 10 products
    top_products = data.groupby("product_name")["sales"].sum().nlargest(10)

    plt.figure()
    top_products.plot(kind="bar")
    plt.title("Top 10 Products by Sales")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.show()

    # Sales by region
    region_sales = data.groupby("region")["sales"].sum()

    plt.figure()
    region_sales.plot(kind="bar")
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()

    # Correlation heatmap
    numeric_data = data.select_dtypes(include=["number"])

    plt.figure()
    sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()