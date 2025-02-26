import re
import pandas as pd
df_base = pd.read_csv('sample_data/batilaptop-01.csv')
columns_to_keep = ['Event Time','Action Type', 'File Name', 'Folder Path', 'Sha1', 'Sha256', 'MD5', 'Process Command Line', 'File Origin Referrer Url', 'Categories','Severities']
df = df_base[columns_to_keep]
df.head()
