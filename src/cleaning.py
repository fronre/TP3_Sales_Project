import pandas as pd


def clean_data(path):

    print("Loading dataset...")

    data = pd.read_csv(path, encoding="ISO-8859-1")

    print("Original shape:", data.shape)

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    # Convert date
    data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])

    # Remove rows without CustomerID
    data.dropna(subset=["CustomerID"], inplace=True)

    # Remove negative or zero quantities
    data = data[data["Quantity"] > 0]

    # Remove negative prices
    data = data[data["UnitPrice"] > 0]

    # Create Sales column
    data["Sales"] = data["Quantity"] * data["UnitPrice"]

    # Extract year and month
    data["Year"] = data["InvoiceDate"].dt.year
    data["Month"] = data["InvoiceDate"].dt.month

    print("Cleaned shape:", data.shape)

    # Save cleaned dataset
    data.to_csv("output/cleaned_data.csv", index=False)

    return data