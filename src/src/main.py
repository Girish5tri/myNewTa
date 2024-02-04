# src/main.py
import pandas as pd

def read_orders_csv(file_path):
    return pd.read_csv(file_path)

def compute_total_revenue_by_month(orders_df):
    orders_df['order_date_month'] = pd.to_datetime(orders_df['order_date']).dt.to_period('M')
    revenue_by_month = orders_df.groupby('order_date_month').agg({'product_price': 'sum'}).reset_index()
    revenue_by_month.columns = ['Month', 'Total Revenue']
    return revenue_by_month

def compute_total_revenue_by_product(orders_df):
    revenue_by_product = orders_df.groupby('product_name').agg({'product_price': 'sum'}).reset_index()
    revenue_by_product.columns = ['Product', 'Total Revenue']
    return revenue_by_product

def compute_total_revenue_by_customer(orders_df):
    revenue_by_customer = orders_df.groupby('customer_id').agg({'product_price': 'sum'}).reset_index()
    revenue_by_customer.columns = ['Customer', 'Total Revenue']
    return revenue_by_customer

def identify_top_customers(revenue_by_customer, top_n=10):
    top_customers = revenue_by_customer.sort_values(by='Total Revenue', ascending=False).head(top_n)
    return top_customers

if __name__ == "__main__":
    orders_df = read_orders_csv('src/orders.csv')

    revenue_by_month = compute_total_revenue_by_month(orders_df)
    print("Total Revenue by Month:\n", revenue_by_month)

    revenue_by_product = compute_total_revenue_by_product(orders_df)
    print("\nTotal Revenue by Product:\n", revenue_by_product)

    revenue_by_customer = compute_total_revenue_by_customer(orders_df)
    print("\nTotal Revenue by Customer:\n", revenue_by_customer)

    top_customers = identify_top_customers(revenue_by_customer)
    print("\nTop 10 Customers by Revenue:\n", top_customers)
