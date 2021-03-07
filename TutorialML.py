#This scripts helps you select rows with multiple filters

#This will use pandas

import Pandas as pd

#At first, create a dataframe  
data = {"name": ["A","B","C","D","E"],
       "score": [1,2,3,4,5]}
df = pd.DataFrame(data)
print(df)
