# IMPORT PANDAS, MATPLOTLIB
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Call the API, read the JSON File and Create a DataFrame
df = pd.read_json("https://data.providenceri.gov/resource/fd8d-n74v.json")

# Step 1: Split Zip values based on '-'
df['zip_postal'] = df['zip_postal'].str.split('-').str[0]

# Step 2: Convert Total Assessment to numeric (if it's not already)
df['total_assmt'] = pd.to_numeric(df['total_assmt'], errors='coerce')

# Step 3: Group by unique Zip and sum Total Assessment
grouped_df = df.groupby('zip_postal')['total_assmt'].sum().reset_index()

# Step 4: Sort by descending order of Total Assessment
grouped_df = grouped_df.sort_values(by='total_assmt', ascending=True)

# Step 5: Plot using horizontal bar chart
plt.figure(figsize=(10, 8))
bars = plt.barh(grouped_df['zip_postal'], grouped_df['total_assmt'])
plt.xlabel('Total Assessment')
plt.ylabel('Zip Code')
plt.title('Tax Assessment by Zip Code')

# Step 6: Display Total Assessment values on the bars with $ prefix and no decimals
for bar, value in zip(bars, grouped_df['total_assmt']):
    plt.text(value, bar.get_y() + bar.get_height() / 2, f'${int(value):,}', ha='right', va='center', color='white')

# Step 7: Remove x-axis values
plt.xticks([])

plt.show()

# Explore the distribution of property assessments, exemptions, and taxes using visualizations such as histograms or box plots.
# extract the relevant columns for analysis
assessments = df['total_assmt'].astype(float)

# Set up the figure and axes for subplots
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))

# Plot histograms for assessments, exemptions, and taxes
sns.histplot(assessments, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Assessments')

# Plot box plots for assessments, exemptions, and taxes
sns.boxplot(x=assessments, ax=axes[0, 1])
axes[0, 1].set_title('Box Plot of Assessments')

# Adjust layout for better readability
plt.tight_layout()
plt.show()

# print(df.dtypes)
