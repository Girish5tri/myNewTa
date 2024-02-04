# tests/test_main.py
import unittest
import pandas as pd
from src.main import read_orders_csv  

class TestMain(unittest.TestCase):
    def test_read_orders_csv(self):

        sample_csv_content = "order_id,customer_id,order_date,product_id,product_name,product_price,quantity\n1,101,2022-01-01,1,ProductA,20.0,2\n2,102,2022-01-02,2,ProductB,30.0,1"
        with open("tests/sample_orders.csv", "w") as sample_csv:
            sample_csv.write(sample_csv_content)

        
        result_df = read_orders_csv("tests/sample_orders.csv")

        
        self.assertIsInstance(result_df, pd.DataFrame)

        
        self.assertEqual(result_df.shape, (2, 7))

        # Check if the DataFrame contains the expected data
        expected_data = {'order_id': [1, 2], 'customer_id': [101, 102], 'order_date': ['2022-01-01', '2022-01-02'],'product_id': [1, 2], 'product_name': ['ProductA', 'ProductB'], 'product_price': [20.0, 30.0], 'quantity': [2, 1]}
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()
