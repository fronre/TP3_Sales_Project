import pandas as pd


def clean_data(path):

    print("Loading dataset...")

    data = pd.read_csv(path)

    print("Initial dataset shape:", data.shape)

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    # Convert date columns
    data['order_date'] = pd.to_datetime(
        data['order_date'],
        format="%d-%m-%Y",
        errors="coerce"
    )

    data['ship_date'] = pd.to_datetime(
        data['ship_date'],
        format="%d-%m-%Y",
        errors="coerce"
    )

    # Convert numeric columns
    numeric_columns = [
        "sales",
        "profit",
        "quantity",
        "discount",
        "shipping_cost"
    ]

    for col in numeric_columns:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    # Remove rows with missing values
    data.dropna(inplace=True)

    # Remove incorrect negative values
    data = data[data["sales"] >= 0]
    data = data[data["quantity"] >= 0]

    # Create new useful columns
    data["order_year"] = data["order_date"].dt.year
    data["order_month"] = data["order_date"].dt.month
    data["profit_margin"] = data["profit"] / data["sales"]

    # Sort data by order date
    data.sort_values(by="order_date", inplace=True)

    print("Cleaned dataset shape:", data.shape)

    # Save cleaned dataset
    data.to_csv("output/cleaned_data.csv", index=False)

    print("Cleaned data saved to output/cleaned_data.csv")

    return data