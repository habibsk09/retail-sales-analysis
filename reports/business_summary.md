# Retail Sales Analysis — Business Summary

## Project Overview

This project demonstrates a retail sales data cleaning and analysis workflow using Python and Pandas. The dataset is synthetic and was created for portfolio and demonstration purposes.

## Key Performance Indicators

| Metric | Result |
|---|---:|
| Total Revenue | ₹10,81,230 |
| Unique Orders | 198 |
| Units Sold | 612 |
| Average Order Value | ₹5,460.76 |

## Key Findings

### 1. Revenue by Product

Monitor generated the highest revenue at ₹6,93,500, contributing approximately 64.1% of total revenue.

### 2. Revenue by City

Kolkata generated the highest revenue at ₹3,98,260, followed by Bangalore at ₹2,97,740.

### 3. Monthly Revenue

- January 2026: ₹4,91,590
- February 2026: ₹1,91,900
- March 2026: ₹3,97,740

Revenue declined in February and recovered in March. More historical data would be required to establish a reliable long-term trend.

## Data Quality Improvements

The raw dataset contained 202 records. The cleaning process:

- Removed 2 exact duplicate records.
- Removed 1 record with an invalid negative quantity.
- Removed 1 record with a missing product.
- Replaced the missing city with `Unknown`.
- Recalculated total amounts using quantity multiplied by unit price.
- Converted the date column to a datetime format.

The resulting cleaned dataset contains 198 records.

## Recommendations

1. Investigate why revenue is heavily concentrated in the Monitor product category.
2. Compare product-level profit margins before making inventory decisions.
3. Investigate monthly revenue fluctuations using additional historical data.
4. Track sales and product performance regularly using a dashboard.

## Limitations

This is a synthetic dataset, not actual business transaction data. Revenue is not the same as profit, and the findings should not be interpreted as evidence about a real business.

## Tools Used

- Python
- Pandas
- Matplotlib
- CSV data processing
