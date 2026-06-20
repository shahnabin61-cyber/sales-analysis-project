# Sales Analysis Project

An end-to-end sales data analysis project using Python, Pandas, SQL, Matplotlib, and Seaborn.

## Project Structure
sales_analysis/

├── data/              # Raw dataset + SQLite database

├── notebooks/         # Jupyter analysis notebook

├── notes/             # Personal cheat sheet

├── sql/               # SQL queries

├── src/               # Python scripts (cleaning + visualization)

├── output/            # Generated charts

└── README.md

## Tools Used
- Python (Pandas, Matplotlib, Seaborn)
- SQLite
- Jupyter Notebook
- Git/GitHub

## Key Insights
- Office Supplies has highest total sales, but lowest profit efficiency
- Furniture has lowest sales, but highest profit efficiency (21.3% margin)
- West region leads in total sales; East region is most efficient
- April has highest monthly sales, January the lowest
- Higher discounts correlate with lower profit (correlation: -0.16)
- Sales strongly predicts profit (correlation: 0.77)

## Charts Generated
- Category sales & profit comparison
- Regional performance
- Monthly sales trend (2021-2023)
- Sub-category profitability
- Discount vs profit relationship
- Correlation heatmap (sales, discount, profit, quantity)

## How to Run
1. Clone the repository
2. Install requirements: `pip install pandas matplotlib seaborn jupyter`
3. Run database setup: `python src/database.py`
4. Generate all charts: `python src/visualizations.py`
5. Explore interactively: `jupyter notebook notebooks/sales_analysis.ipynb`