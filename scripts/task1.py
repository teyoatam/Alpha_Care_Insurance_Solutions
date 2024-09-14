import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the insurance data
file_path ='../data/MachineLearningRating_v3.txt'
data = pd.read_csv(file_path, sep='|', low_memory=False)

def data_understanding(data):
    # Data Understanding
    print(data.head())
    print(data.info())

def Catagoriy_data(data):
  obj = (data.dtypes == 'object')
  object_cols = list(obj[obj].index)
  print("Categorical variables:",len(object_cols))

  int_ = (data.dtypes == 'int')
  num_cols = list(int_[int_].index)
  print("Integer variables:",len(num_cols))

  fl = (data.dtypes == 'float')
  fl_cols = list(fl[fl].index)
  print("Float variables:",len(fl_cols))
  

def data_summarization(data):
    # Print all column names in the DataFrame
    print("Column names:")
    print(data.columns.tolist())

    # Calculate descriptive statistics for numerical features
    numerical_features = ['TotalPremium', 'TotalClaims', 'PolicyID']
    for feature in numerical_features:
        if feature in data.columns:
            print(f"Descriptive statistics for '{feature}':")
            print(data[feature].describe())
            print()
        else:
            print(f"Column '{feature}' not found in the DataFrame.")

    # Review data types
    print("\nColumn data types:")
    print(data.dtypes)

def data_quality_assessment(data):
    # Check for missing values
    print(data.isnull().sum())


def univariate_analysis(data):
    # Plot histograms for numerical columns
    plt.figure(figsize=(10, 6))
    sns.histplot(data['TotalPremium'], bins=20, kde=True)
    plt.title('Distribution of Total Premium')
    plt.show()

    # Create bar charts for categorical columns
    plt.figure(figsize=(10, 6))
    sns.countplot(data['CoverType'])
    plt.title('Frequency of Cover Type')
    plt.show()
    

def bivariate_multivariate_analysis(data):
    # Explore correlations and associations between variables
    corr_matrix = data[['TotalPremium', 'TotalClaims', 'PostalCode']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

    # Scatter plot for TotalPremium vs TotalClaims based on mmcode
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='TotalPremium', y='TotalClaims', hue='PostalCode', data=data)
    plt.title('TotalPremium vs TotalClaims by PostalCode')
    plt.show()




def plot_premium_vs_region(data):
    """
    Create a scatter plot to compare insurance premiums by region.
    Args:
        data (pd.DataFrame): Input data containing 'TotalPremium' and 'Country'.
    """
    sns.scatterplot(data=data, x='Country', y='TotalPremium')
    plt.xlabel('Region')
    plt.ylabel('Total Premium')
    plt.title('Insurance Premiums by Region')
    plt.show()

def plot_cover_type_distribution(data):
    """
    Create a bar chart to show the distribution of insurance cover types by region.
    Args:
        data (pd.DataFrame): Input data containing 'CoverType' and 'Country'.
    """
    sns.countplot(data=data, x='CoverType', hue='Country')
    plt.xlabel('Cover Type')
    plt.ylabel('Count')
    plt.title('Distribution of Insurance Cover Types by Region')
    plt.show()

def plot_auto_make_distribution(data):
    """
    Create a bar chart to show the distribution of auto makes by region.
    Args:
        data (pd.DataFrame): Input data containing 'make' and 'Country'.
    """
    sns.countplot(data=data, x='make', hue='Country')
    plt.xlabel('Auto Make')
    plt.ylabel('Count')
    plt.title('Distribution of Auto Makes by Region')
    plt.show()

# Usage
plot_premium_vs_region(data)
plot_cover_type_distribution(data)
plot_auto_make_distribution(data)


def plot_boxplot(data, column_name):
    """
    Create a box plot for a numerical column.
    Args:
        data (pd.DataFrame): Input data.
        column_name (str): Name of the column.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data[column_name])
    plt.title(f'Box Plot of {column_name}')
    plt.xlabel(column_name)
    plt.show()

# Usage
plot_boxplot(data, 'TotalPremium')
plot_boxplot(data, 'TotalClaims')