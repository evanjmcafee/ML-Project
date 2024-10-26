import pandas as pd
import numpy as np
df = pd.DataFrame()
data = {'Name':[],'Year':[],'Month':[],'Day':[], 'Hour':[], 'Minute':[], 'OS':[], 'RAM Usage':[], 'EXE':[],'Window':[],'Last Page':[]}

df = pd.DataFrame(data)
df.to_csv('Log.csv')
print(df)

