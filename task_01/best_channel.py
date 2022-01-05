import pandas as pd
import numpy as np
df = pd.read_csv(r'D:\Sensix\Python\Tarefa1\overlap_values.csv')

dictFinal = {}
for j in range(2, df.shape[1]):
    spaceColor = {}
    for i in range(len(df.index)):
        if (df.loc[i][j].replace('.', '', 1).isdigit()):
            keys2 = df.loc[i][1].strip()
            valueChannel = float(df.loc[i][j])
            listSpaceColor = []
            listSpaceColor = spaceColor[keys2] \
                if keys2 in spaceColor else listSpaceColor
            listSpaceColor.append(valueChannel)
            spaceColor[keys2] = listSpaceColor
    keys1 = df.columns[j]
    dictFinal[keys1] = spaceColor

for channel, dictColor in dictFinal.items():
    for color, listColor in dictColor.items():
        dictColor[color] = np.mean(listColor)

df2 = pd.DataFrame(dictFinal)
df2 = df2.assign(Best_Overlap=df2.min(axis=1))
df2 = df2.assign(Best_Channel=None)
df2 = df2.rename_axis('Space Color').reset_index()
df2 = df2.sort_values(by=['Best_Overlap'])

for i in range(len(df2.index)):
    for j in range(1, df2.shape[1]-2):
        value = df2.loc[i][4]
        comparison = df2.loc[i][j]
        if value == comparison:
            df2.at[i, 'Best_Channel'] = df.columns[j+1]
        else:
            pass

dc = pd.DataFrame(df2, columns=["Space Color", "Best_Overlap", "Best_Channel"])
dc.to_csv(r'D:\Sensix\Python\Tarefa1\teste2.csv', index=False)
