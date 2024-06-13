import pandas as pd

def check_header(file_path):
    # Read the first few rows of the CSV file assuming there is a header
    df_with_header = pd.read_csv(file_path, nrows=5)
    
    # Read the first few rows of the CSV file without a header
    df_without_header = pd.read_csv(file_path, nrows=5, header=None)
    print(df_with_header)
    print(df_without_header)
    # Compare the first row of the df_with_header with the column names of df_without_header
    if list(df_with_header.columns) == list(df_without_header.iloc[0]):
        return True  # The file has a header
    else:
        return False  # The file does not have a header

# Example usage
file_path = '/workspace/boilerplate-demographic-data-analyzer/adult.data.csv'
has_header = check_header(file_path)
if has_header:
    print("The CSV file has a header.")
else:
    print("The CSV file does not have a header.")
