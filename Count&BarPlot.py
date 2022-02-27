#DataCamp - Introduction to Data Visulization with Seaborn
#Chapter3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
survey_data = pd.read_csv('/home/mukul/PycharmProjects/Seaborn/Data/young-people-survey-responses.csv')
condition = [(survey_data['Age'] >= 21) ,
             (survey_data['Age'] < 21)]
values=['21+', 'Less than 21']
survey_data['age_category'] = np.select(condition, values)
#survey_data['age_category'] = np.where(survey_data['Age']>=21, True, False)
#print(survey_data[['Age', 'age_category']])
print(survey_data.info())
#print(survey_data['Mathematics'].head(10))

#sns.catplot(y='Internet usage', data=survey_data, kind='count', col='Age')
sns.catplot(y='Age', data=survey_data, kind='count')
plt.show()