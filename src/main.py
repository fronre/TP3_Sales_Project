from cleaning import clean_data
from analysis import run_analysis

def main():
    data = clean_data("data/sales_data.csv")
    run_analysis(data)

if __name__ == "__main__":
    main()