#DataCamp - Introduction to Data Visulization with Seaborn
#Chapter2 - Seaborn RelPlots
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
student_data = pd.read_csv("/home/mukul/PycharmProjects/Seaborn/student-alcohol-consumption.csv")
print(student_data.info())
#sns.relplot(x='absences', y='G3', data=student_data, kind='scatter', row='study_time')
sns.relplot(x='G1', y='G3', data=student_data, kind='scatter', col='schoolsup', col_order=['yes', 'no'],
            row='famsup', row_order=['yes', 'no'])
plt.show()