"""This module will be used to get data ready
"""
import pandas as pd

def get_data(path):
    """This funct loads data

    Args:
        path (str): load data into dataframe
    """
    data = pd.read_csv(path)
    data.info()