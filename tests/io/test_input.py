import pytest
import pandas as pd
from app.io.input import read_file, read_file_with_pandas


def test_read_file_exists():
    """
    Test that the read_file function returns a non-empty list for an existing file.
    """
    test_filename = 'test.csv'
    # Assuming 'test.csv' exists and contains data separated by commas
    result = read_file(test_filename)
    assert result, "The result should not be empty for an existing file"


def test_read_file_content():
    """
    Test that the read_file function returns correct content.
    """
    test_filename = 'test.csv'
    # Create a test file with known content
    with open(test_filename, 'w') as f:
        f.write('LalaLand')
    result = read_file(test_filename)
    assert result == ['LalaLand'], "The header row should be correctly read"


def test_read_file_nonexistent():
    """
    Test that the read_file function raises an exception for a nonexistent file.
    """
    with pytest.raises(FileNotFoundError):
        read_file('nonexistent.csv')


def test_read_file_with_pandas_exists():
    """
    Test that the read_file_with_pandas function returns a DataFrame for an existing file.
    """
    test_filename = 'test_pandas.csv'
    # Assuming 'test_pandas.csv' exists and is in proper CSV format
    result = read_file_with_pandas(test_filename)
    assert isinstance(result, pd.DataFrame), "The result should be a pandas DataFrame"


def test_read_file_with_pandas_content():
    """
    Test that the read_file_with_pandas function returns correct content.
    """
    test_filename = 'test_pandas.csv'
    # Create a test file with known content
    with open(test_filename, 'w') as f:
        f.write('col1,col2\nvalue1,value2')
    result = read_file_with_pandas(test_filename)
    assert result['col1'][0] == 'value1', "The DataFrame should contain the correct value in col1"
    assert result['col2'][0] == 'value2', "The DataFrame should contain the correct value in col2"


def test_read_file_with_pandas_nonexistent():
    """
    Test that the read_file_with_pandas function raises an exception for a nonexistent file.
    """
    with pytest.raises(FileNotFoundError):
        read_file_with_pandas('nonexistent.csv')
