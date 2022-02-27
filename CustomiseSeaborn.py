#DataCamp - Introduction to Data Visulization with Seaborn
#Chapter2 - Seaborn RelPlots
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
mpg = pd.read_csv("/home/mukul/PycharmProjects/Seaborn/mpg.csv")
#print(mpg.info())
#sns.relplot(x='horsepower', y='mpg', data=mpg, kind='scatter', size='cylinders', hue='cylinders')
#sns.relplot(x='acceleration', y='mpg', data=mpg, kind='scatter', hue='origin', style='origin')
#sns.relplot(x='model_year', y='mpg', data=mpg, kind='line')
#sns.relplot(x='model_year', y='mpg', data=mpg, kind='line', ci='sd')
sns.relplot(x='model_year', y='horsepower', data=mpg, kind='line', ci=None, style='origin', hue='origin',
            markers=True, dashes=False)

plt.show()