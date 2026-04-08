# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sports_data.csv")

# Display first 5 rows
print("Dataset Preview:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Average performance
avg_performance = df['Performance'].mean()
print("\nAverage Performance:", avg_performance)

# Top performing player/team
top_player = df.loc[df['Performance'].idxmax()]
print("\nTop Performer:")
print(top_player)

# Team-wise average performance
team_avg = df.groupby('Team')['Performance'].mean()
print("\nAverage Performance by Team:")
print(team_avg)

# Visualization - Bar chart
plt.figure(figsize=(8,5))
sns.barplot(x=team_avg.index, y=team_avg.values)
plt.title("Average Performance by Team")
plt.xlabel("Team")
plt.ylabel("Performance")
plt.xticks(rotation=45)
plt.show()

# Visualization - Histogram
plt.figure(figsize=(8,5))
plt.hist(df['Performance'], bins=10)
plt.title("Performance Distribution")
plt.xlabel("Performance")
plt.ylabel("Frequency")
plt.show()

# Year vs Performance trend (if Year column exists)
if 'Year' in df.columns:
    year_avg = df.groupby('Year')['Performance'].mean()

    plt.figure(figsize=(10,5))
    plt.plot(year_avg.index, year_avg.values, marker='o')
    plt.title("Average Performance Over Years")
    plt.xlabel("Year")
    plt.ylabel("Performance")
    plt.show()