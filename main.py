#DataCamp - Introduction to Data Visulization with Seaborn
#Chapter5
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
countries = pd.read_csv("/home/mukul/PycharmProjects/Seaborn/countries-of-the-world.csv")
print(countries.info())
gdp = countries['GDP ($ per capita)']
phones = countries['Phones (per 1000)']
percent_literate = countries['Literacy (%)']
region = countries['Region']
#sns.scatterplot(x=gdp, y=percent_literate)
sns.countplot(y=region)
plt.show()

