import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


def run_analysis(data):
    """
    Perform Exploratory Data Analysis (EDA)
    """

    print("\n===== Descriptive Statistics =====")
    print(data.describe())

    # Sales trend over years
    sales_over_time = data.groupby(data["order_date"].dt.year)["sales"].sum()

    plt.figure()
    sales_over_time.plot(kind="line", marker="o")
    plt.title("Sales Trend Over Years")
    plt.xlabel("Year")
    plt.ylabel("Total Sales")
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


def customer_segmentation(data):
    """
    Apply KMeans clustering for simple customer segmentation
    """

    print("\n===== Customer Segmentation using KMeans =====")

    # Select features
    X = data[["sales", "profit"]]

    # Apply KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    data["cluster"] = kmeans.fit_predict(X)

    # Plot clusters
    plt.figure()
    plt.scatter(data["sales"], data["profit"], c=data["cluster"])
    plt.title("Customer Segmentation")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.show()

    return data