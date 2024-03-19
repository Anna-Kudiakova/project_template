from app.io.input import read_console, read_file, read_file_with_pandas
from app.io.output import console_output, file_output


def main():
    console_input = read_console()
    file_input = read_file('input.csv')
    file_input_pandas = read_file_with_pandas('input_pandas.csv')
    console_output(console_input)
    console_input(file_input)
    console_output(file_input_pandas)
    file_output(console_input, 'output.csv')
    file_output(file_input_pandas, 'output_pandas.csv')


if __name__ == '__main__':
    main()
