import pandas as pd
import numpy as np

df = pd.read_csv("employee_data.csv")

print("🔍 Original Data:")
prin
df = df.drop_duplicates()
print("\n✅ Removed duplicates")

df['name'] = df['name'].fillna("Unknown")
df['email'] = df['email'].fillna("unknown@company.com")

df['salary'] = df['salary'].fillna(df['salary'].median())

df['joining_date'] = df['joining_date'].fillna("1900-01-01")

print("\n✅ Handled missing values")

df['email'] = df['email'].apply(lambda x: x if "@" in str(x) else "unknown@company.com")

print("\n✅ Fixed invalid emails")

department_map = {
    "HR": "Human Resources",
    "hr": "Human Resources",
    "Information Technology": "IT"
}
df['department'] = df['department'].replace(department_map)

print("\n✅ Standardized department names")

df['salary'] = pd.to_numeric(df['salary'], errors='coerce')  # convert to number
df['salary'] = df['salary'].apply(lambda x: np.nan if x <= 0 else x)  # remove invalid (0 or negative)
df['salary'] = df['salary'].fillna(df['salary'].median())  # replace invalid with median

print("\n✅ Cleaned salary data")

df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')

today = pd.Timestamp.today()
df.loc[df['joining_date'] > today, 'joining_date'] = pd.NaT

df['joining_date'] = df['joining_date'].fillna(df['joining_date'].median())

print("\n✅ Cleaned joining_date")

df.to_csv("employee_data_cleaned.csv", index=False)

print("\n🎉 Data cleaning complete! Saved to employee_data_cleaned.csv")
print("\n📊 Cleaned Data:")
print(df)
