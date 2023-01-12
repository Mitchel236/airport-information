import pandas as pd
from datetime import datetime

data = [['12/01/2023','D2','B738','',61000,'10:33','11:37'],
        ['12/01/2023','D3','B738','',57800,'13:48','15:35'],
        ['12/01/2023','D1','B738','',59100,'16:33','17:10']


]

df = pd.DataFrame(data, columns=['DATE', 'STAND', 'TYPE', 'HEAVY', 'WEIGHT', 'ARRIVAL', 'DEPARTURE'])

df['ARRIVAL'] =  pd.to_datetime(df['ARRIVAL'])
df['DEPARTURE'] =  pd.to_datetime(df['DEPARTURE'])

df['ARRIVAL'] = df['ARRIVAL'].dt.time
df['DEPARTURE'] = df['DEPARTURE'].dt.time

# df['ΔDEP/ARR'] = (df['DEPARTURE'].sub(df['ARRIVAL'])) 

df.to_csv("./datasets/test-dataframe.csv")