#DataCamp - Introduction to Data Visulization with Seaborn
#Chapter3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
student_data = pd.read_csv('/home/mukul/PycharmProjects/Seaborn/Data/student-alcohol-consumption.csv')
category_order = ["<2 hours",
                  "2 to 5 hours",
                  "5 to 10 hours",
                  ">10 hours"]
#print(student_data.info())
#print(student_data['study_time'])

sns.catplot(x='study_time', y='G3', data=student_data, kind='bar', order=category_order, ci=None)
plt.show()