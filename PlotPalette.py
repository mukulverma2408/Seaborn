import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
survey_data = pd.read_csv("/home/mukul/PycharmProjects/Seaborn/Data/young-people-survey-responses.csv", index_col=0)
print(survey_data.info())
#print(survey_data["Parents Advice"])
#category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]
#sns.catplot(x="Parents' advice", data=survey_data,  kind="count", order=category_order)
sns.catplot(x='Siblings', y='Loneliness', data=survey_data, kind='bar')
plt.show()