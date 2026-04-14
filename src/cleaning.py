import pandas as pd


def clean_data(path):

    print("Loading dataset...")

    data = pd.read_csv(path, encoding="ISO-8859-1")

    print("Original shape:", data.shape)

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    # Convert date
    data["InvoiceDate"] = pd.to_datetime(data["order_date"], format='mixed', errors='coerce')

    # Drop rows with invalid dates
    data.dropna(subset=["InvoiceDate"], inplace=True)

    # Remove rows without CustomerID
    data.dropna(subset=["customer_name"], inplace=True)

    # Remove negative or zero quantities
    data = data[data["quantity"] > 0]

    # Since UnitPrice not available, use sales as Sales
    data["Sales"] = pd.to_numeric(data["sales"], errors='coerce')
    data.dropna(subset=["Sales"], inplace=True)
    data["Quantity"] = pd.to_numeric(data["quantity"], errors='coerce')
    data.dropna(subset=["Quantity"], inplace=True)
    data["Description"] = data["product_name"]
    data["Country"] = data["country"]
    data["CustomerID"] = data["customer_name"]

    # Extract year and month
    data["Year"] = data["InvoiceDate"].dt.year
    data["Month"] = data["InvoiceDate"].dt.month

    print("Cleaned shape:", data.shape)

    # Save cleaned dataset
    data.to_csv("output/cleaned_data.csv", index=False)

    return data