from cleaning import clean_data
from analysis import run_analysis, customer_segmentation


def main():

    print("===== Starting Data Analysis Project =====")

    # Step 1: Clean the dataset
    data = clean_data("data/SuperStoreOrders.csv")

    # Step 2: Run Exploratory Data Analysis
    run_analysis(data)

    # Step 3: Apply Machine Learning (Customer Segmentation)
    data = customer_segmentation(data)

    print("===== Project Completed Successfully =====")


if __name__ == "__main__":
    main()