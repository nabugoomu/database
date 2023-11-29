import unittest
import pandas as pd
import app
import data

class CalculationTests(unittest.TestCase):

    def test_add_columns(self):
        # Create sample data
        data_df = pd.DataFrame(
            {
                "Column1": [1, 2, 3],
                "Column2": [4, 5, 6],
            }
        )

        # Perform calculations
        calculated_data = app.perform_calculations(data_df)

        # Check if new column is added
        self.assertIn("Total", calculated_data.columns)

        # Check if addition is correct
        self.assertEqual(calculated_data["Total"].tolist(), [5, 7, 9])

    def test_calculate_average(self):
        # Create sample data
        data_df = pd.DataFrame(
            {
                "Column3": [10, 20, 30],
            }
        )

        # Perform calculations
        calculated_data = app.perform_calculations(data_df)

        # Check if new column is added
        self.assertIn("Average", calculated_data.columns)

        # Check if average is correct
        self.assertEqual(calculated_data["Average"].tolist(), [20.0])


if __name__ == "__main__":
    unittest.main()
