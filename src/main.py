from cleaning import clean_data
from analysis import run_analysis, customer_segmentation


def main():
    data = clean_data("data/data.csv")
    run_analysis(data)

    customer_segmentation(data)


if __name__ == "__main__":
    main()