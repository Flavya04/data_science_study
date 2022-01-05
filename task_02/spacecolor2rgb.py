import pandas as pd
df_rgb = pd.read_csv(r'D:\Sensix\Python\Tarefa2\RGB.csv')
df_rgbTo = pd.read_csv(r'D:\Sensix\Python\Tarefa2\rgb2hed.csv')

df_end = pd.concat([df_rgbTo.idxmax(), df_rgbTo.idxmin(), df_rgbTo.max(
), df_rgbTo.min()], axis=1, keys=['Index max', 'Index Min', 'Max', 'Min'])
df_end = df_end.rename_axis('Channel').reset_index()
df_end['Max RGB'] = df_end['Min RGB'] = None


for j in range(1, df_end.shape[1]-4):
    for i in range(df_end.shape[0]):
        index = df_end.loc[i][j]
        value_rgb = df_rgb.loc[index].values
        df_end.iat[i, j+4] = value_rgb

df_end = pd.DataFrame(
    df_end, columns=["Channel", "Max", "Min", "Max RGB", "Min RGB"])

df_end
