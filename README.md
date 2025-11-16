# Task-2 Student Performance Exploratory Data Analysis (EDA)

## Overview
This project performs Exploratory Data Analysis (EDA) on the `student-mat.csv` dataset.  
The objective is to understand the dataset using summary statistics, visualizations, and correlation analysis to uncover patterns, trends, and anomalies.

## Dataset
- **File Name:** `student-mat.csv`
- **Source:** Student Performance Dataset
- **Features:** Contains numeric and categorical variables related to student academic performance.
- **Separator:** `;`

## Tools & Libraries
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Logging

## Steps Performed
1. **Load Dataset**
    - Read the CSV file using Pandas
    - Display first few rows and dataset info

2. **Data Overview**
    - Check for missing values
    - Identify numeric columns

3. **Summary Statistics**
    - Compute mean, median, standard deviation, skewness, and kurtosis for numeric columns

4. **Univariate Analysis**
    - Plot histograms for numeric columns
    - Plot boxplots for outlier detection

5. **Correlation Analysis**
    - Compute correlation matrix
    - Plot correlation heatmap

6. **Outlier & Anomaly Detection**
    - Check skewness
    - Identify potential outliers using IQR method

## Hints / Mini Guide
- Generate summary statistics: mean, median, standard deviation, skewness, kurtosis
- Create histograms and boxplots for numeric features
- Use pairplot/correlation matrix to analyze relationships
- Identify patterns, trends, or anomalies in the data
- Make basic inferences from visuals

