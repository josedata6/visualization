import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# generate data
x = np.linspace(1, 10, 300)
y = np.log(x)

plt.figure(figsize=(5,3))
plt.plot(x, y, color='#168aad', linewidth=10, linestyle='dotted')
plt.gca().set_facecolor('#99d98c')
plt.grid()
plt.show()

# generate data
revenue = [5000, 7000, 8000, 6500, 7200, 9000]
months = ['January', 'February', 'March', 'April', 'May', 'June']

# visualize
plt.figure(figsize=(5, 3))
sns.lineplot(x=months, y=revenue, marker='D', markersize=10,
             color='#bb9457', linestyle='dashed', linewidth=2)
plt.gca().set_facecolor('#f8edeb')
plt.grid()
plt.show()

df = pd.read_csv('student.csv')
df.head()

# count data items
len(df)

df['gender'].value_counts()

sns.countplot(data=df, x='gender', hue='gender',
              palette={'female':'#ffb5a7', 'male':'#168aad'})
plt.show()

sns.catplot(data=df, x='gender', kind='count', hue='gender',
              palette={'female':'#ffb5a7', 'male':'#168aad'})
plt.show()

## showing the dog image of dog plot :)
##sns.dogplot()

sns.catplot(data=df, x='gender', y='math_score', hue='lunch', kind='bar',
            palette={'standard':'#6f1d1b', 'free/reduced':'#bb9457'})
plt.show()

sns.catplot(data=df, x='gender', y='math_score', kind='swarm')
plt.show()

# sample data
sample_df = df.iloc[0:200, :]
sample_df.shape

sns.catplot(data=sample_df, y='gender', x='math_score', kind='swarm',
            hue='lunch', palette={'standard':'#ee9b00', 'free/reduced':'#5a189a'})
plt.show()

sns.catplot(data=sample_df, y='gender', x='math_score', kind='violin',
            hue='lunch', palette={'standard':'#ee9b00', 'free/reduced':'#5a189a'})
plt.show()