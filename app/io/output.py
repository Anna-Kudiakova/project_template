
def console_output(data):
    """
    Print the provided data to the console.

    Args:
        data (str): The data to be printed.
    """
    print(f'Data from the file: \n {data}')


def file_output(data, filename):
    """
    Write the provided data to a file.

    Args:
        data (str): The data to be written to the file.
        filename (str): The name of the file to write the data into the 'data' directory.
    """
    with open(f'./data/{filename}', 'w') as file:
        file.write(data)
