from cleaning import clean_data
from analysis import run_analysis


def main():
    # Step 1: Clean the dataset
    data = clean_data("data/SuperStoreOrders.csv")

    # Step 2: Run EDA analysis
    run_analysis(data)


if __name__ == "__main__":
    main()