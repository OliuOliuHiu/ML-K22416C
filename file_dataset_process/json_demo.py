import pandas as pd
df = pd.read_csv("../dataset/SalesTransactions.json",
                 encoding ='utf-8', dtype ='unicode',
                sep='\t',
                low_memory=False)
print(df)