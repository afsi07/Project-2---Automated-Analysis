# /// script
# dependencies = [
#   "httpx",
#   "pandas",
#   "seaborn",
#   "scipy",
#   "matplotlib",
#   "numpy",
#   "tabulate",
# ]
# ///
import os
import argparse
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Get the token from the environment variable
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")

# Function to create directories if they do not exist
def ensure_directories_exist(directories):
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            with open(os.path.join(directory, "README.md"), "w") as f:
                f.write(f"# {directory.capitalize()} Analysis\n\nPlaceholder README for {directory} analysis.")

# Function to handle missing values and outliers
def preprocess_data(df):
    # Handle missing values
    missing_summary = df.isnull().sum()
    df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill numeric NaNs with mean

    # Detect and remove outliers using Z-scores
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    z_scores = np.abs((df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std())
    df_cleaned = df[(z_scores < 3).all(axis=1)]

    return df_cleaned, missing_summary

# Function to generate visualizations
def generate_visualizations(df, output_dir):
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True, color='skyblue')
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, f"{col}_distribution.png"))
        plt.close()

    if len(numeric_cols) >= 2:
        plt.figure(figsize=(8, 8))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", square=True)
        plt.title("Correlation Heatmap")
        plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
        plt.close()

        sns.pairplot(df[numeric_cols], diag_kind='kde', plot_kws={'alpha': 0.7})
        plt.savefig(os.path.join(output_dir, "pairplot.png"))
        plt.close()

# Function to generate Markdown narratives
def generate_narrative(df, missing_summary, output_dir):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()

    insights = []
    insights.append("# Dataset Analysis\n")
    insights.append("## Summary Statistics\n")
    insights.append(df.describe().to_markdown())
    insights.append("\n\n## Missing Values\n")
    insights.append(missing_summary.to_markdown())
    insights.append("\n\n## Correlation Matrix\n")
    insights.append(corr_matrix.to_markdown())

    insights.append("\n\n## Key Insights\n")
    for col in numeric_cols:
        insights.append(f"- **{col}:** Mean = {df[col].mean():.2f}, Std Dev = {df[col].std():.2f}, Skewness = {df[col].skew():.2f}, Kurtosis = {df[col].kurt():.2f}")

    insights.append("\n\n## Visualizations\n")
    insights.append("Refer to the generated PNG files for detailed visualizations, including distribution histograms and correlation heatmaps.")

    with open(os.path.join(output_dir, "README.md"), "w") as f:
        f.write("\n".join(insights))

# Main function to process datasets
def process_dataset(dataset_path, output_dir):
    try:
        df = pd.read_csv(dataset_path, encoding='ISO-8859-1')
        df_cleaned, missing_summary = preprocess_data(df)
        generate_visualizations(df_cleaned, output_dir)
        generate_narrative(df_cleaned, missing_summary, output_dir)
    except Exception as e:
        print(f"Error processing {dataset_path}: {e}")

# Script entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze datasets and generate narratives and visualizations.")
    parser.add_argument("dataset", help="Path to the input dataset (CSV file).")
    args = parser.parse_args()

    # Define output directories
    output_dirs = ["goodreads", "happiness", "media"]
    ensure_directories_exist(output_dirs)

    # Determine appropriate output directory
    dataset_name = os.path.basename(args.dataset).split('.')[0].lower()
    output_dir = next((d for d in output_dirs if dataset_name in d), "output")
    ensure_directories_exist([output_dir])

    # Process the dataset
    process_dataset(args.dataset, output_dir)
