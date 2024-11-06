import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('student.csv')
df.head()

# create a histogram for math_score
plt.figure(figsize=(4, 3))
sns.histplot(data=df, x='math_score')
plt.show()

# specify the different bins
plt.figure(figsize=(4,3))
sns.histplot(data=df, x='math_score', color='#588157',
             binwidth=6, fill=False)
plt.show()

plt.figure(figsize=(4,3))
sns.histplot(data=df, x='math_score', color='#588157',
             binwidth=6, fill=False, kde=True)
plt.show()

# kdeplot is a probability
plt.figure(figsize=(4,3))
sns.kdeplot(data=df, x='math_score', color='orange',
            linewidth=4, fill=True)
plt.show()

plt.figure(figsize=(4, 3))
sns.histplot(data=df, x='math_score', hue='gender',
             palette={'female':'#ef233c', 'male':'#0096c7'},
             kde=True, fill=False, binwidth=8)
plt.show()

plt.figure(figsize=(4, 3))
sns.kdeplot(data=df, x='math_score', hue='gender',
             palette={'female':'#ef233c', 'male':'#0096c7'},
            )
plt.show()

# how to visualize the math_score distribution across
# test_preparation_course
plt.figure(figsize=(8, 3))
sns.kdeplot(data=df, x='math_score', hue='test_preparation_course',
          palette={'none':'grey','completed':'green'},
            fill=True)
plt.show()

plt.figure(figsize=(8,3))
sns.histplot(data=df, x='math_score', hue='test_preparation_course',
             palette={'none':'grey','completed':'green'},
             kde=True, element='step')
plt.show()

# explore the math_score distribution across ethnicity
# palette='Dark2'
plt.figure(figsize=(8,3))
sns.kdeplot(data=df, x='math_score', hue='ethnicity',
             palette='Dark2', common_norm=True)
plt.show()

# create boxplot to explore math distribution across ethnicity
plt.figure(figsize=(8,3))
sns.catplot(data=df, x='ethnicity', y='math_score',
             hue='ethnicity', palette='Set1', kind='box')
plt.show()

sns.boxplot(data=df, x='math_score')
plt.show()

# explore the relationship between math and reading
plt.figure(figsize=(4, 3))
sns.scatterplot(data=df, x='reading_score', y='math_score',
                hue='gender', palette={'female':'#ef233c', 'male':'#0096c7'},
             )
plt.show()

plt.figure(figsize=(4, 3))
sns.scatterplot(data=df, x='reading_score', y='writing_score',
                hue='gender', palette={'female':'#ef233c', 'male':'#0096c7'},
             )
plt.show()