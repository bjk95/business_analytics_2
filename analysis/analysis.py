import pandas as pd


def describe_data():
    df = pd.read_excel("../data/2020 T2 MIS171 Assignment 2.xlsx", sheet_name="Survey Data")

    print(df.columns)
    print(df.describe())
    print(df.head())


def run():
    describe_data()


if __name__ == "__main__":
    run()
