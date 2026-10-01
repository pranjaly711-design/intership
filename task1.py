import pandas as pd

# Load CSV file
df = pd.read_csv("netflix_titles.csv")

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert date column
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Save cleaned file
df.to_csv("netflix_titles_cleaned.csv", index=False)

print("Data cleaning completed!")
print(df.head())
