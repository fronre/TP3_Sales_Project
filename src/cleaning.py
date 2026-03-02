import pandas as pd

def clean_data(path):

    data = pd.read_csv(path)

    data.drop_duplicates(inplace=True)

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
    data['sales'] = pd.to_numeric(data['sales'], errors='coerce')
    data['profit'] = pd.to_numeric(data['profit'], errors='coerce')
    data['quantity'] = pd.to_numeric(data['quantity'], errors='coerce')
    data['discount'] = pd.to_numeric(data['discount'], errors='coerce')
    data['shipping_cost'] = pd.to_numeric(data['shipping_cost'], errors='coerce')

    data.dropna(inplace=True)

    data.to_csv("output/cleaned_data.csv", index=False)

    return data