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