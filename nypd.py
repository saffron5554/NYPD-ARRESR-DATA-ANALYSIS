import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\python_project\NYPD_Arrest_Data_2023.csv")

# Check the first few rows of the dataset
print(df.head())

# Data cleaning and preprocessing

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values in crucial columns, if necessary
df = df.dropna(subset=['ARREST_DATE', 'ARREST_BORO', 'AGE_GROUP', 'PERP_SEX', 'PERP_RACE'])

# Convert ARREST_DATE to datetime
df['ARREST_DATE'] = pd.to_datetime(df['ARREST_DATE'], errors='coerce')

# Check for duplicate rows
print(f"Duplicate Rows: {df.duplicated().sum()}")

# Remove duplicates if any
df = df.drop_duplicates()

# Descriptive statistics of numerical columns
print(df.describe())

# Data Exploration and Visualizations

# 1. Distribution of arrests over time (ARREST_DATE)
plt.figure(figsize=(10, 6))
df['ARREST_DATE'].dt.month.value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Monthly Arrests in 2023')
plt.xlabel('Month')
plt.ylabel('Number of Arrests')
plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.show()

# 2. Arrests by Borough (ARREST_BORO)
plt.figure(figsize=(10, 6))
df['ARREST_BORO'].value_counts().plot(kind='bar', color='salmon')
plt.title('Arrests by Borough')
plt.xlabel('Borough')
plt.ylabel('Number of Arrests')
plt.xticks(rotation=45)
plt.show()

# 3. Arrests by Age Group (AGE_GROUP)
plt.figure(figsize=(10, 6))
df['AGE_GROUP'].value_counts().sort_index().plot(kind='bar', color='lightgreen')
plt.title('Arrests by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Arrests')
plt.xticks(rotation=45)
plt.show()

# 4. Arrests by Perpetrator Sex (PERP_SEX)
plt.figure(figsize=(8, 5))
df['PERP_SEX'].value_counts().plot(kind='bar', color='lightcoral')
plt.title('Arrests by Perpetrator Sex')
plt.xlabel('Gender')
plt.ylabel('Number of Arrests')
plt.xticks(rotation=45)
plt.show()

# 5. Arrests by Perpetrator Race (PERP_RACE)
plt.figure(figsize=(12, 6))
df['PERP_RACE'].value_counts().plot(kind='bar', color='lightblue')
plt.title('Arrests by Perpetrator Race')
plt.xlabel('Race')
plt.ylabel('Number of Arrests')
plt.xticks(rotation=45)
plt.show()

# 6. Arrests by Crime Type (OFNS_DESC and PD_DESC)
# OFNS_DESC: Offense Description
# PD_DESC: PD (Police Department) Code Description
plt.figure(figsize=(14, 6))
df['OFNS_DESC'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title('Top 10 Offense Types')
plt.xlabel('Offense Description')
plt.ylabel('Number of Arrests')
plt.xticks(rotation=45)
plt.show()

# 7. Arrests by Crime Law Category (LAW_CAT_CD)
plt.figure(figsize=(8, 6))
df['LAW_CAT_CD'].value_counts().plot(kind='bar', color='yellowgreen')
plt.title('Arrests by Law Category')
plt.xlabel('Law Category')
plt.ylabel('Number of Arrests')
plt.xticks(rotation=45)
plt.show()

# 8. Plot arrests on a scatter plot based on Latitude and Longitude
plt.figure(figsize=(10, 6))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5, color='purple', s=1)
plt.title('Geospatial Distribution of Arrests')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

df['hour'] = df['ARREST_DATE'].dt.hour
df['day_of_week'] = df['ARREST_DATE'].dt.dayofweek
df['month'] = df['ARREST_DATE'].dt.month

# Extract day of the week from ARREST_DATE
df['day_of_week'] = df['ARREST_DATE'].dt.dayofweek

# 9. Plot arrests by day of the week
plt.figure(figsize=(10, 6))
df.groupby('day_of_week').size().plot(kind='bar', color='lightcoral')
plt.title('Arrests by Day of the Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Arrests')
plt.xticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], rotation=45)
plt.show()

# 10. Plot correlation between age group and arrest count for different offenses
df['AGE_GROUP'] = df['AGE_GROUP'].astype('category').cat.codes  # Convert age groups to numerical values
df.groupby('AGE_GROUP')['OFNS_DESC'].value_counts().unstack().plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Arrests by Age Group and Crime Type')
plt.xlabel('Age Group')
plt.ylabel('Number of Arrests')
plt.xticks(rotation=45)
plt.show()
