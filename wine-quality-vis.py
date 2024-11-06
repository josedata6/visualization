import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# load the data
df = pd.read_csv('winequality.csv')
df.head()

# check the quality level distribution
sns.countplot(data=df, x='quality', hue='quality', palette='YlGn',
              stat='percent')
plt.show()

# explore sulphate's mean(avg) and std across the quality
# as the quality goes up the sulphates level goes up
plt.figure(figsize=(7, 4))
sns.pointplot(data=df, x='quality', y='sulphates', linestyle='--',
              marker='*', markersize=15, mfc='steelblue', mec='#ffca3a',
              color='#ff0054')
plt.grid(axis='y', linewidth=0.5, color='#ff0054')
plt.show()

# explore the avg and std for sulphates and volatile acidity across wine quality
plt.figure(figsize=(7, 4))
sns.pointplot(data=df, x='quality', y='sulphates', linestyle='--',
              marker='X', markersize=15, mfc='steelblue', mec='skyblue',
              color='#ba181b', label='sulphates')
sns.pointplot(data=df, x='quality', y='volatile acidity', linestyle='-',
              marker='o', markersize=10, mfc='lightgreen', mec='gold',
              color='#8ac926', label='volatile acidity')
plt.grid(axis='y', linewidth=0.6, color='#3772ff')
plt.ylabel('value')
plt.legend()
plt.show()
# as the qulity goes up the acidity goes down

# explore the range (min, avg, max) of sulphates across wine quality
plt.figure(figsize=(7, 4))
sns.pointplot(data=df, x='quality', y='sulphates', errorbar=('pi', 100),
              capsize=0.2, linestyle='none', marker='+', markersize=10,
              mfc='#a4161a', mec='skyblue', color='#fdc500')
plt.show()

# explore the distribution of "citric acid" and its avg across wine quality
plt.figure(figsize=(7,4))
sns.stripplot(data=df, x='quality', y='citric acid', color='#f4a259', alpha=0.5)
sns.pointplot(data=df, x='quality', y='citric acid', linestyle='none', errorbar=None,
              marker="_", color='#00509d', markersize=15)
plt.show()

# changing styles
plt.figure(figsize=(7,4))
sns.stripplot(data=df, x='quality', y='citric acid', color='#007200', alpha=0.5,
              jitter=False, marker='*', linewidth=0.2, s=15)
plt.show()

# dispolayig data
# heatmap
df.head()

# explore the correlation coefficient among these numeric variables
# extract all numeric variables
new_df = df.iloc[:, 0:11]
new_df.head()

# compute the correlation coefficient
coco = new_df.corr()
coco

# visualize the coco
plt.figure(figsize=(10,10))
sns.heatmap(coco, square=True, cmap='bwr_r', linewidth=0.5, vmin=-1, vmax=1)
plt.xticks(rotation=30)
plt.show()

# remove the half of the square
# add numbers
tri_matrix = np.triu(coco)
tri_matrix

# visualize the half coco
plt.figure(figsize=(10,10))
sns.heatmap(coco, square=True, cmap='bwr_r', linewidth=0.5, vmin=-1, vmax=1,
            mask = tri_matrix, annot=True, fmt='.2f')
plt.xticks(rotation=30)
plt.title('Correlation Coefficient among Variables')
plt.show()

# explore the relationship between 'fixed acidity' and 'alcohol'
plt.figure(figsize=(7,4))
sns.scatterplot(data=df, x='fixed acidity', y='alcohol', color='#ccff33')
sns.histplot(data=df, x='fixed acidity', y='alcohol', pthresh=0.1)
sns.kdeplot(data=df, x='fixed acidity', y='alcohol')
plt.show()

plt.figure(figsize=(7,4))
sns.kdeplot(data=df, x='sulphates', y='alcohol', hue='quality', levels=5)
plt.show()