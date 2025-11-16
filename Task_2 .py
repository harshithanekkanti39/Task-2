import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os

sns.set(style="whitegrid")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# Create a folder to save plots
os.makedirs("plots", exist_ok=True)

# Load dataset
def load_dataset(path, sep=";"):
    try:
        df = pd.read_csv(path, sep=sep)
        logging.info(f"Loaded dataset. Shape: {df.shape}")
        return df
    except Exception as e:
        logging.error(f"Could not load dataset: {e}")
        return None

df = load_dataset("student-mat.csv")
if df is None:
    raise SystemExit("Dataset could not be loaded.")

numeric_cols = df.select_dtypes(include=np.number).columns

# Dataset overview
def dataset_overview(df):
    print("\n--- First 5 Rows ---")
    display(df.head())
    print("\n--- Dataset Info ---")
    print(df.info())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

dataset_overview(df)

# Summary statistics
def summary_statistics(df):
    print("\n--- Summary Statistics ---")
    display(df.describe().T)
    print("\n--- Numeric Column Insights ---")
    for col in numeric_cols:
        print(
            f"{col}: Mean={df[col].mean():.2f}, "
            f"Median={df[col].median():.2f}, "
            f"Std={df[col].std():.2f}, "
            f"Skew={df[col].skew():.2f}, "
            f"Kurt={df[col].kurtosis():.2f}"
        )

summary_statistics(df)

# Univariate analysis
def plot_histograms(df):
    df[numeric_cols].hist(figsize=(16, 12), bins=20)
    plt.suptitle("Histogram of Numeric Columns", fontsize=16)
    plt.tight_layout()
    plt.savefig("plots/histograms.png")
    plt.close()
    logging.info("Saved histograms.png")

def plot_boxplots(df):
    plt.figure(figsize=(16, 7))
    sns.boxplot(data=df[numeric_cols], orient="h")
    plt.title("Boxplots (Outlier Check)")
    plt.savefig("plots/boxplots.png")
    plt.close()
    logging.info("Saved boxplots.png")

plot_histograms(df)
plot_boxplots(df)

# Correlation heatmap
def correlation_analysis(df):
    plt.figure(figsize=(14, 10))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("plots/correlation_heatmap.png")
    plt.close()
    logging.info("Saved correlation_heatmap.png")

correlation_analysis(df)

# Outlier & anomaly check
def detect_anomalies(df):
    print("\n--- Outlier & Skewness Check ---")
    for col in numeric_cols:
        skew = df[col].skew()
        if abs(skew) > 1:
            print(f"{col}: High skew → might need transformation")
        Q1, Q3 = df[col].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
        if len(outliers) > 0:
            print(f"{col}: {len(outliers)} potential outliers detected")

detect_anomalies(df)

logging.info("All plots saved in the 'plots/' folder.")
