import pandas as pd
#col_name=['operation', 'time']
#df = pd.read_csv('/home/mukul/PycharmProjects/Seaborn/Data/testing.csv', header=None, names=col_name)
#print(df.head())
#uniq = df['operation'].unique()

#new_df = df.groupby('operation')['time'].mean()
#print(new_df)
#for i in uniq:
#    print(i, end='~~~')
#    print(df[df['operation'] == i]['time'].min(), end='~~~')
#    print(df[df['operation'] == i]['time'].max())
#string='MukulVermaMukulVermaMukulMukul'
#print(string[::-1])
#print(string.count('Mukul'))

#file = open('/home/mukul/PycharmProjects/Seaborn/Data/testing.csv', 'r')
#data = file.read()
#word = ['operation1', 'operation2', 'operation3']
#for i in word:
#    counter = data.count(i)
#    print(i, end='~~~')
#    print(counter)

#marks = {'Malika':[52,56,60],
#         'Arjun':[70,98,63],
#         'Krishna' :[67,68,69]}

#print(marks['Malika'])
#print(len(marks['Malika']))
#print(sum(marks['Malika']))


list = [1, 2, 4, 5, 7, 8, 2, 6]
new_list=[ x for x in list ]
print(new_list)

