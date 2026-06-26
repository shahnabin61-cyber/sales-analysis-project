# My Pandas + Seaborn Cheat Sheet
*Built from my own Sales Analysis project — patterns I actually use*

---

## Loading & Exploring Data

```python
df = pd.read_csv('path/to/file.csv')
df.shape                    # (rows, columns)
df.columns.tolist()         # list of column names
df.head()                   # first 5 rows
df.dtypes                   # data type of each column
df.isnull().sum()           # count missing values per column
df.describe()               # statistics: mean, min, max, etc.
```

---

## Fixing Dates

```python
df['date_col'] = pd.to_datetime(df['date_col'])
df['year'] = df['date_col'].dt.year
df['month'] = df['date_col'].dt.month
```

**Combining year+month into a date:**
```python
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
```

---

## Grouping & Aggregating (the core pattern!)

```python
# Pattern: df.groupby('column')['target'].function()

df.groupby('category')['sales'].sum()
df.groupby('category')[['sales', 'profit']].sum()
df.groupby(['region', 'sub_category'])['profit'].sum()  # multiple group keys
```

**Sorting results:**
```python
.sort_values('sales', ascending=False)
```

**IMPORTANT:** after groupby, the grouped column becomes the INDEX, not a column!
```python
.reset_index()   # turns index back into a normal column
```

---

## Finding Max/Min Rows

```python
df['sales'].max()              # just the VALUE
df['sales'].idxmax()           # the ROW INDEX of the max
df.loc[df['sales'].idxmax()]   # the WHOLE ROW with the max value
```

---

## Calculating Custom Metrics (like efficiency)

```python
df['efficiency'] = df['profit'] / df['sales']
df['efficiency_percentage'] = df['efficiency'] * 100
```

---

## Top N per Group

```python
# Top 3 sub_categories per region, by profit
top3 = df.sort_values('profit', ascending=False) \
          .groupby('region') \
          .head(3) \
          .sort_values('region')
```

---

## Matplotlib Charts

**Bar chart (vertical):**
```python
fig, ax1 = plt.subplots(figsize=(12, 5))
my_summary['sales'].plot(kind='bar', ax=ax1, color=['#2196F3', '#4CAF50', '#FF9800'])
ax1.set_title('My Title')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')
ax1.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('output/chart.png', dpi=150)
plt.show()
```

**Bar chart (horizontal) — note x/y labels flip!**
```python
my_summary['sales'].plot(kind='barh', ax=ax1, color=[...])
ax1.set_xlabel('Sales ($)')   # x and y are SWAPPED vs vertical bar
ax1.set_ylabel('Category')
```

**Line chart (for trends over time):**
```python
plt.plot(df['date'], df['sales'], color='#2196F3', marker='o')
plt.title('Trend Over Time')
plt.xticks(rotation=45)
```

---

## Seaborn Charts

```python
sns.set_style('whitegrid')   # nicer default look

# IMPORTANT: use already-grouped data for TOTALS,
# raw df will show AVERAGE (with confidence interval bars)
sns.barplot(x=my_summary.index, y=my_summary['sales'])
```

---

## Color Codes I Use

```python
colors = [
    '#2196F3',  # Blue
    '#4CAF50',  # Green
    '#FF9800',  # Orange
    '#E91E63',  # Pink
    '#9C27B0',  # Purple
    '#F44336'   # Red
]
```

---

## Common Mistakes I've Made (so I don't repeat them!)

- Forgot `reset_index()` → got "column not found" errors when grouped column became the index
- Used `plt.show()` inside a `.py` script → froze the terminal (only use in notebooks!)
- Horizontal bar chart → forgot xlabel/ylabel swap from vertical version
- Re-running notebook after reopening VS Code → all variables gone, need "Run All" first





## Machine Learning (scikit-learn) — Core Pattern

```python
from sklearn.[module] import [ModelName]
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Define features and target
X = df[['feature1', 'feature2']]  # inputs (uppercase X)
y = df['target']                   # what to predict (lowercase y)

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train
model = ModelName()
model.fit(X_train, y_train)

# 4. Predict
y_pred = model.predict(X_test)

# 5. Evaluate
mae = mean_absolute_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)
```

## Algorithms I've used:
```python
# Regression (predict numbers):
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Classification (predict YES/NO):
from sklearn.linear_model import LogisticRegression
```

## Evaluation Metrics: