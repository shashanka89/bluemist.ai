import pandas as pd


def get_data():
    data = pd.read_csv("datasets/auto-mpg/auto-mpg.csv")
    return data