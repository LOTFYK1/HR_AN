import pandas as pd

# Load cleaned data
df = pd.read_csv("HR_data_cleaned.csv")

# 1. First 5 rows
print(df.head())

# 2. Column info
print(df.info())

# 3. Summary statistics for numbers
print(df.describe())

# 4. Job distribution
print(df['Department'].value_counts())

# 5. Attrition counts
print(df['Attrition'].value_counts())

# 6. Average Age, Salary, Years at Company by Attrition
print(df.groupby('Attrition')[['Age','Salary','YearsAtCompany']].mean())

# 7. Min and Max for numbers
print(df[['Age','Salary','YearsAtCompany']].agg(['min','max']))

# 8. Check missing values
print(df.isna().sum())
