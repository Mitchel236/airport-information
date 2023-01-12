import pandas as pd
from datetime import datetime

data = [['12/01/2023','', '', '', '', '', '7:28'],
        ['12/01/2023','A1', '', '', '', '', '10:25'],
        ['12/01/2023', 'B1', '', '', '', '20:49', ''],
        ['12/01/2023', 'B2', '', '', '', '', '7:17'],
        ['12/01/2023', 'B2', '', '', '', '14:20', '15:53'],
        ['12/01/2023', 'B2', '', '', '', '21:18', ''],
        ['12/01/2023', 'C1', '', '', '', '14:13', '15:03'],
        ['12/01/2023', 'C2', '', '', '', '', '7:10'],
        ['12/01/2023', 'C2', '', '', '', '10:03', '10:35'],
        ['12/01/2023', 'C2', '', '', '', '18:07', '18:54'],
        ['12/01/2023', 'C3', '', '', '', '', '7:30'],
        ['12/01/2023', 'D1', '', '', '', '11:40', '15:56'],
        ['12/01/2023', 'D1', '', '', '', '16:31', '17:23'],
        ['12/01/2023', 'D1', '', '', '', '17:26', '18:20'],
        ['12/01/2023', 'D1', '', '', '', '21:38', ''],
        ['12/01/2023', 'D2', '', '', '', '', '7:04'],
        ['12/01/2023', 'D2', '', '', '', '10:31', '11:32'],
        ['12/01/2023', 'D2', '', '', '', '12:40', '13:40'],
        ['12/01/2023', 'D2', '', '', '', '13:48', '15:40'],
        ['12/01/2023', 'D2', '', '', '', '20:34', ''],
        ['12/01/2023', 'D3', '', '', '', '21:42', '']


]

df = pd.DataFrame(data, columns=['DATE', 'STAND', 'TYPE', 'HEAVY', 'WEIGHT', 'ARRIVAL', 'DEPARTURE'])

df['ARRIVAL'] =  pd.to_datetime(df['ARRIVAL'])
df['DEPARTURE'] =  pd.to_datetime(df['DEPARTURE'])

df['ARRIVAL'] = df['ARRIVAL'].dt.time
df['DEPARTURE'] = df['DEPARTURE'].dt.time

# df['ΔDEP/ARR'] = (df['DEPARTURE'].sub(df['ARRIVAL'])) 

df.to_csv("./datasets/test-dataframe.csv")




