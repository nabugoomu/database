import pandas as pd
import openpyxl

def read_excel_data(data_path):
    """Read data from an Excel file into a Pandas DataFrame."""
    # Read Excel file into DataFrame
    data_df = pd.read_excel(data_path, sheet_name="Data")
    return data_df

def write_excel_data(data_df, output_data_path):
    """Write data from a Pandas DataFrame to an Excel file."""
    # Create a new Excel workbook
    wb = openpyxl.Workbook()

    # Create a new worksheet and write DataFrame data
    ws = wb.active
    ws.append(data_df.columns.tolist())
    for index, row in data_df.iterrows():
        ws.append(row.tolist())

    # Save the Excel file
    wb.save(output_data_path)
