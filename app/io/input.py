import pandas as pd
from pathlib import Path


def read_console():
    """
    Prompt the user to enter their name via the console and return it.

    Returns:
        str: The name entered by the user.
    """
    name = input('Enter your name: ')
    return name


def read_file(filename):
    """
    Read the contents of a file and return a list of lines split by comma.

    Args:
        filename (str): The name of the file to read from the 'data' directory.

    Returns:
        list of str: A list of strings, where each string is a line in the file split by comma.
    """
    data_folder = Path(__file__).parent.parent / 'data'
    file_path = data_folder / filename
    with file_path.open('r') as file:
        lines = file.readlines()
    return lines


def read_file_with_pandas(filename):
    """
    Read a CSV file into a pandas DataFrame.

    Args:
        filename (str): The name of the CSV file to read from the 'data' directory.

    Returns:
        DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    data_folder = Path(__file__).parent.parent / 'data'
    file_path = data_folder / filename
    file_df = pd.read_csv(file_path)
    return file_df
