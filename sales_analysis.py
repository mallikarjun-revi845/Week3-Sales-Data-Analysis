"""
Project : Week 3 - Sales Data Analysis
Intern  : Mallikarjun Revi
Language: Python
Library : Pandas
"""

import pandas as pd

print("=" * 70)
print("             SALES DATA ANALYSIS USING PANDAS")
print("=" * 70)

# Load Dataset

print("\nLoading Dataset...")
df = pd.read_csv("sales_data.csv")

# Dataset Overview

print("\nDataset Loaded Successfully!")

print("\nDataset Shape")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumn Names")
print(df.columns.tolist())

print("\nFirst 5 Records")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# Missing Values

print("\nMissing Values")
print(df.isnull().sum())

df.fillna(0, inplace=True)

# Duplicate Records

duplicates = df.duplicated().sum()
print(f"\nDuplicate Records Found : {duplicates}")

df.drop_duplicates(inplace=True)

# Business Metrics

total_revenue = df["Total_Sales"].sum()
average_sale = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()

best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

print("\n" + "=" * 70)
print("                 SALES SUMMARY")
print("=" * 70)

print(f"Total Revenue        : ₹{total_revenue:,.2f}")
print(f"Average Sale         : ₹{average_sale:,.2f}")
print(f"Highest Sale         : ₹{highest_sale:,.2f}")
print(f"Lowest Sale          : ₹{lowest_sale:,.2f}")
print(f"Best Selling Product : {best_product}")

print("\nRevenue by Product")
print(df.groupby("Product")["Total_Sales"].sum())

print("\nRevenue by Region")
print(df.groupby("Region")["Total_Sales"].sum())

print("\nTop 5 Products")
print(df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).head())

with open("sales_report.txt","w") as report:
    report.write("SALES DATA ANALYSIS REPORT\n")
    report.write("="*50+"\n")
    report.write(f"Total Revenue : ₹{total_revenue:,.2f}\n")
    report.write(f"Average Sale : ₹{average_sale:,.2f}\n")
    report.write(f"Highest Sale : ₹{highest_sale:,.2f}\n")
    report.write(f"Lowest Sale : ₹{lowest_sale:,.2f}\n")
    report.write(f"Best Product : {best_product}\n")

print("\nReport Generated Successfully (sales_report.txt)")
print("=" * 70)
