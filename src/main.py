from cleaning import clean_data

def main():
    data = clean_data("data/SuperStoreOrders.csv")
    print("Data cleaned successfully")
    print(data.head())

if __name__ == "__main__":
    main()