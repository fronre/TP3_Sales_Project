import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


def run_analysis(data):
    """
    Perform Exploratory Data Analysis (EDA)
    """

    print("\n===== Descriptive Statistics =====")
    print(data.describe())

    # Sales trend over time
    sales_trend = data.groupby(data["InvoiceDate"].dt.date)["Sales"].sum()

    plt.figure()
    sales_trend.plot()
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Top 10 products
    top_products = data.groupby("Description")["Sales"].sum().nlargest(10)

    plt.figure()
    top_products.plot(kind="bar")
    plt.title("Top 10 Products by Sales")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.show()

    # Sales by country
    country_sales = data.groupby("Country")["Sales"].sum()

    plt.figure()
    country_sales.plot(kind="bar")
    plt.title("Sales by Country")
    plt.xlabel("Country")
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
    Customer segmentation using KMeans
    """

    print("\n===== Customer Segmentation (KMeans) =====")

    # Aggregate customer data
    customer_data = data.groupby("CustomerID").agg({
        "Sales": "sum",
        "Quantity": "sum"
    }).reset_index()

    # Apply clustering
    X = customer_data[["Sales", "Quantity"]]

    kmeans = KMeans(n_clusters=3, random_state=42)
    customer_data["cluster"] = kmeans.fit_predict(X)

    # Plot clusters
    plt.figure()
    plt.scatter(customer_data["Sales"], customer_data["Quantity"], c=customer_data["cluster"])
    plt.title("Customer Segmentation")
    plt.xlabel("Total Sales")
    plt.ylabel("Quantity Purchased")
    plt.tight_layout()
    plt.show()

    return customer_data