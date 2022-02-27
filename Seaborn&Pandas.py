#DataCamp - Introduction to Data Visulization with Seaborn
#Chapter5
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("/home/mukul/PycharmProjects/Seaborn/young-people-survey-responses.csv")
#print(df.info())
sns.countplot(x='Spiders', data=df)
plt.show()