import pandas as pd

def clean_data(path):
    """
    Load and clean the sales dataset.
    - Remove duplicates
    - Handle missing values
    - Convert date columns
    """

    # Load dataset
    data = pd.read_csv(path)

    # Remove duplicate rows
    data.drop_duplicates(inplace=True)

    # Convert date columns to datetime
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['ship_date'] = pd.to_datetime(data['ship_date'])

    # Remove missing values
    data.dropna(inplace=True)

    # Save cleaned dataset
    data.to_csv("output/cleaned_data.csv", index=False)

    return data