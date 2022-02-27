#DataCamp - Introduction to Data Visulization with Seaborn
#Chapter3 - Seaborn BoxPlot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median
student_data = pd.read_csv("/home/mukul/PycharmProjects/Seaborn/Data/student-alcohol-consumption.csv")
#print(student_data.info())
#sns.catplot(x='internet', y='G3', data=student_data, kind='box', hue='location', sym='')
#sns.catplot(x="romantic", y="G3",data=student_data,kind="box",whis=[0,100])
#sns.catplot(x='famrel', y='absences', data=student_data, kind='point', capsize=0.2, join=False)
sns.catplot(x='romantic', y='absences', data=student_data, kind='point', hue='school', ci=None, estimator=median)
plt.show()