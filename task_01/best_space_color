import pandas as pd
df = pd.read_csv(r'D:\Sensix\Python\Tarefa1\overlap_values.csv')

spaceColorSum = {}
for i in range(len(df.index)):
    if (df.loc[i]['Channel_1'] != 'Channel_1'):
        keys = df.loc[i]['Space Collor'].strip()
        channelSum = float(df.loc[i]['Channel_1']) + \
            float(df.loc[i]['Channel_2']) + float(df.loc[i]['Channel_3'])
        value = spaceColorSum[keys] + \
            channelSum if keys in spaceColorSum else channelSum
        spaceColorSum[keys] = value
spaceColor = list(spaceColorSum.keys())
sColor = list(spaceColorSum.values())
print(spaceColor)
print(sColor)
