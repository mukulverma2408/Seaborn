#DataCamp - Introduction to Data Visulization with Seaborn
#Chapter5
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
student_data = pd.read_csv("/home/mukul/PycharmProjects/Seaborn/student-alcohol-consumption.csv")
palette_color = {'Rural': 'green', 'Urban': 'blue'}
#sns.scatterplot(x='absences', y='G3', data=student_data, hue='location', hue_order=['Rural','Urban'])
#plt.show()
sns.countplot(x='school', data=student_data, hue='location', palette=palette_color)
plt.show()
