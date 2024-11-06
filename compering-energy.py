# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# reading file
df = pd.read_csv('energy.csv')
df.head()

# 1. Load the dataset into colab and create a line chart showing the commercial energy generation over time.
plt.figure(figsize=(26, 5))
plt.plot_date(x=df['Date'], y = df['commercial'], linewidth=2,
              c='blue', markersize=12, mfc='#ffbe0b', mec='grey', fmt='X--',)
plt.gcf().autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Commercial Energy Generation Over Time')
plt.grid()
plt.title('Commercial Energy Generation Over 2001-2004')
plt.show()

# 2. Create one figure that display both commercial energy generations over time together.
# plotting both commercial & industrial in same plot
plt.figure(figsize=(26, 5))

# plot the industrial with a label for the legend
sns.lineplot(data=df, x='Date', y='industrial', marker='X', markersize=10, linestyle='-',
             mfc='grey', mec='grey', c='grey', label='Industrial')

# plot the commercial with a label for the legend
sns.lineplot(data=df, x='Date', y='commercial', marker='o', markersize=9, linestyle='--',
             mfc='gold', mec='gold', c='gold', label='Commercial')

# Add legend
plt.legend(title="Line Type")

# Add grid, title, and format the x-axis dates
plt.grid()
plt.title('Commercial & Industrial Energy Generations Over 2001-2004')
plt.gcf().autofmt_xdate()

# Show the plot
plt.show()

# converting file to html from Google colab
##!jupyter nbconvert --to html HW2_BANA610.ipynb