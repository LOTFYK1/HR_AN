import pandas as pd
df = pd.read_csv('HR_data_cleaned.csv')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df['Employeeid'] = df['Employeeid'].astype(str)
df['Age'] = df['Age'].astype(int)
df['Deparment'] = df['Deparment'].astype(str)
df['salary'] = df['salary'].astype(float)
df['yearsAtCompany'] = df['yearsAtCompany'].astype(int)
df['Attrition'] = df['Attrition'].astype(str)
df.to_csv('HR_data_cleaned.csv', index=False)

print("Data cleaned and saved as 'HR_data_cleaned.csv'")
