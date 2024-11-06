import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib_venn import venn2

# generate data, for two products
prod = [500, 300]
prod_name = ['iPhone', 'iPad']
colors = ['#fb5607', '#344e41']

# visualize pie chart
plt.figure(figsize=(3, 3))
plt.pie(prod, labels=prod_name, colors=colors, autopct='%1.1f%%')
plt.show()

# generate data
svy_values = [100, 200, 100, 150, 90]
svy_labels = ['strongly agree', 'agree', 'neither', 'disagree', 'strongly disagree']
svy_colors = ['#0fa3b1', '#b5e2fa', '#f9f7f3', '#eddea4', '#f7a072']

plt.figure(figsize=(4,4))
plt.pie(svy_values, labels=svy_labels, colors=svy_colors, autopct='%1.1f%%')
plt.show()

df = pd.read_csv('student.csv')
df.head()

# display the gender distribution by using pie chart
df['gender'].value_counts()

gender_value = df['gender'].value_counts().tolist()
gender_value

gender_name = df['gender'].value_counts().index.tolist()
gender_name

gender_color = ['#edafb8','#6a994e']

plt.figure(figsize=(3,3))
plt.pie(gender_value, labels=gender_name, colors=gender_color, autopct='%1.1f%%')
plt.show()

# create pie chart for the ethnicity
# define your own variable names
# select color palette (*)

# display the ethnicity distribution by using pie chart
df['ethnicity'].value_counts()

ethnicity_value = df['ethnicity'].value_counts().tolist()
ethnicity_value

ethnicity_type = df['ethnicity'].value_counts().index.tolist()
ethnicity_type

ethnicity_color = ['#edafb8','#6a994e', '#03045e', '#415a77', '#ef233c']

plt.figure(figsize=(3,3))
plt.pie(ethnicity_value, labels=ethnicity_type, colors=ethnicity_color, autopct='%1.1f%%')
plt.show()

# from matplotlib_venn import venn2
a = set(['orange', 'apple', 'iphone', 'lambo'])
b = set(['apple', 'cake'])

venn2(subsets=(a, b), set_labels=('a', 'b'), set_colors=('skyblue','lightgreen'))
plt.title('Venn Diagram from Sets a and b')
plt.show()

venn = venn2(subsets=(a, b), set_labels=('a', 'b'), set_colors=('skyblue','lightgreen'))
venn.get_label_by_id('10').set_text(', '.join(a-b))
venn.get_label_by_id('11').set_text(', '.join(a&b))
venn.get_label_by_id('01').set_text(', '.join(b-a))
plt.title('Venn Diagram with Elements from Sets a & b')
plt.show()