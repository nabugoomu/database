import app
import data

# Load data from Excel file
data_path = "data.xlsx"
data_df = data.read_excel_data(data_path)

# Perform calculations using Pandas
calculated_data = app.perform_calculations(data_df)

# Save calculated data to Excel file
output_data_path = "output.xlsx"
data.write_excel_data(calculated_data, output_data_path)