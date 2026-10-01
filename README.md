Netflix Data Cleaning Project

Objective
Clean and preprocess the Netflix Titles dataset to improve data quality and prepare it for analysis.

Dataset
Netflix Titles Dataset (netflix_titles.csv)

Data Cleaning Steps Performed
Checked for missing values using isnull().sum()
Removed duplicate records using drop_duplicates()
Standardized column names by converting them to lowercase and replacing spaces with underscores
Converted the date_added column to datetime format
Exported the cleaned dataset to a new CSV file

Files Included

task1.py – Python script used for data cleaning
netflix_titles.csv – Original dataset
netflix_titles_cleaned.csv – Cleaned dataset

Tools Used
Python
Pandas
GitHub Codespaces

Outcome

The dataset was cleaned by handling data quality issues, standardizing column names, removing duplicate entries, and formatting date fields for further analysis.

Deliverables
✅ Cleaned Dataset: netflix_titles_cleaned.csv
✅ Python Script: task1.py
✅ Summary Report: README.md
