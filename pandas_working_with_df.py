import pandas as pd
import numpy as np

def read_csv_dataset(csv_path, header):
    if header:
        df = pd.read_csv(csv_path, header=0)
    else:
        df = pd.read_csv(csv_path, header=None)


def get_first_n_entries(dataframe, n):
    return dataframe.head(n)


def get_last_n_entries(dataframe, n):
    return dataframe.tail(n)


def assign_headers(dataframe, headers):
    dataframe.columns = headers
    return dataframe


def replace_question_marks_to_nan(dataframe):
    dataframe = dataframe.replace('?', np.nan)
    return dataframe


def get_dtypes(dataframe):
    return dataframe.dtypes


def get_description(dataframe):
    return dataframe.describe()


def get_summary(dataframe):
    return dataframe.info()


def save_df_to_csv(dataframe, save_path):
    dataframe.to_csv(save_path)