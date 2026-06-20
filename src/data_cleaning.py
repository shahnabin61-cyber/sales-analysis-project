import pandas as pd

def load_and_clean_data():
    # Load data
    df = pd.read_csv('data/superstore.csv')
    
    # Convert date to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # Add year and month columns
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    
    # Add efficiency column
    df['efficiency'] = df['profit'] / df['sales']
    
    print("Data cleaned successfully!")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    
    return df

# Run if this file is executed directly
if __name__ == '__main__':
    df = load_and_clean_data()