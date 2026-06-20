import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
import seaborn as sns

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_cleaning import load_and_clean_data

def plot_category_analysis(df):
    category_summary = df.groupby('category')[['sales', 'profit']].sum()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    category_summary['sales'].plot(kind='bar', ax=ax1, color=['#2196F3','#4CAF50','#FF9800'])
    ax1.set_title('Total Sales by Category')
    ax1.set_xlabel('Category')
    ax1.set_ylabel('Sales ($)')
    ax1.tick_params(axis='x', rotation=45)

    category_summary['profit'].plot(kind='bar', ax=ax2, color=['#2196F3','#4CAF50','#FF9800'])
    ax2.set_title('Total Profit by Category')
    ax2.set_xlabel('Category')
    ax2.set_ylabel('Profit ($)')
    ax2.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.savefig('output/category_analysis.png', dpi=150)
  
    print("Category chart saved!")

def plot_region_analysis(df):
    region_summary = df.groupby('region')[['sales', 'profit']].sum().sort_values('sales', ascending=False)
    
    fig, ax1 = plt.subplots(figsize=(10, 5))
    
    region_summary['sales'].plot(kind='bar', ax=ax1, color=['#2196F3','#4CAF50','#FF9800','#E91E63'])
    ax1.set_title('Total Sales by Region')
    ax1.set_xlabel('Region')
    ax1.set_ylabel('Sales ($)')
    ax1.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('output/region_analysis.png', dpi=150)
    print("Region chart saved!")

def plot_monthly_trend(df):
    monthly_sales = df.groupby(['year', 'month'])['sales'].sum().reset_index()
    monthly_sales['date'] = pd.to_datetime(monthly_sales[['year', 'month']].assign(day=1))
    
    plt.figure(figsize=(14, 5))
    plt.plot(monthly_sales['date'], monthly_sales['sales'], color='#2196F3', marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/monthly_trend.png', dpi=150)
    print("Monthly trend chart saved!")

def plot_subcategory_analysis(df):
    subcategory_summary = df.groupby('sub_category')[['sales', 'profit']].sum().sort_values('profit', ascending=False)
    
    fig, ax1 = plt.subplots(figsize=(12, 5))
    
    subcategory_summary['sales'].plot(kind='barh', ax=ax1, color=[
        '#2196F3', '#4CAF50', '#FF9800', '#E91E63', '#9C27B0', '#F44336'
    ])
    ax1.set_title('Total Sales by Subcategory')
    ax1.set_xlabel('Sales ($)')
    ax1.set_ylabel('Sub-Category')
    
    plt.tight_layout()
    plt.savefig('output/subcategory_analysis.png', dpi=150)
    print("Subcategory chart saved!")

def plot_discount_analysis(df):
    discount_analysis = df.groupby('discount')[['sales', 'profit']].mean().reset_index()
    
    plt.figure(figsize=(14, 5))
    plt.plot(discount_analysis['discount'], discount_analysis['profit'], color='#2196F3', marker='o')
    plt.title('Discount vs Profit')
    plt.xlabel('Discount (%)')
    plt.ylabel('Profit ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/discount_analysis.png', dpi=150)
    print("Discount chart saved!")

def plot_correlation_heatmap(df):
    correlation_data = df[['sales', 'discount', 'profit', 'quantity']].corr()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_data, annot=True, fmt='.2f', cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('output/correlation_heatmap.png', dpi=150)
    print("Correlation heatmap saved!")

if __name__ == '__main__':
    df = load_and_clean_data()
    plot_category_analysis(df)
    plot_region_analysis(df)
    plot_monthly_trend(df)
    plot_subcategory_analysis(df)
    plot_discount_analysis(df)
    plot_correlation_heatmap(df)