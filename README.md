# Sales Analysis Project

This repository contains a Python-based workflow for loading, cleaning, and visualizing a Superstore sales dataset. The project focuses on exploring sales performance, profit trends, regional behavior, and discount effects using Pandas, Matplotlib, Seaborn, and Jupyter.

## Project Overview

The analysis pipeline currently includes:
- Loading the raw CSV dataset from the data folder
- Cleaning and enriching the data with date-based fields and an efficiency metric
- Generating visualizations for product categories, regions, monthly sales, subcategories, discount impact, and correlations
- Providing a notebook for interactive exploration

## Repository Structure

- data/ - Raw dataset files, including superstore.csv
- notebooks/ - Jupyter notebook for exploratory analysis
- notes/ - Reference notes and cheat sheets
- output/ - Generated chart images
- sql/ - SQL queries related to the dataset
- src/ - Python source files
  - data_cleaning.py - Loads and cleans the dataset
  - visualizations.py - Creates charts and saves them to output/
  - database.py - Placeholder for future database-related functionality

## Requirements

Install the required Python packages with:

```bash
pip install pandas matplotlib seaborn jupyter
```

## How to Run

From the project root, run:

1. Clean and prepare the data:
   ```bash
   python src/data_cleaning.py
   ```

2. Generate the charts:
   ```bash
   python src/visualizations.py
   ```

3. Open the notebook for interactive analysis:
   ```bash
   jupyter notebook notebooks/sales_analysis.ipynb
   ```

## Generated Outputs

The visualization script saves the following images in the output/ folder:
- category_analysis.png
- region_analysis.png
- monthly_trend.png
- subcategory_analysis.png
- discount_analysis.png
- correlation_heatmap.png

## Notes

- The scripts are designed to be run from the project root.
- The database module is currently empty and can be expanded later for SQLite or other database integration.
- The analysis is based on the Superstore dataset and focuses on business-facing insights such as profitability, regional performance, and sales seasonality.

## Key Business Insights
- Office Supplies has highest total sales but lowest profit efficiency
- Furniture has lowest sales but highest profit efficiency (21.3% margin)
- West region leads in total sales; East region is most efficient
- April has highest monthly sales, January the lowest
- Higher discounts correlate with lower profit (correlation: -0.16)
- Sales strongly predicts profit (correlation: 0.77)

## Statistics Analysis
- Distribution analysis (mean, median, standard deviation)
- Outlier detection using IQR method (found 12 high-profit outliers!)
- Correlation heatmap across sales, discount, profit, quantity
- Normal distribution visualization with mean and std dev lines
- Box plots showing sales spread by category
