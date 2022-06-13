"""This module will be used to get data ready
"""
import pandas as pd

def get_data(io):
    data = pd.read_excel(io)
    data.info()