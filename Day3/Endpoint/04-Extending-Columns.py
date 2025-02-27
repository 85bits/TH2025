import pandas as pd
df_base = pd.read_csv('sample_data/batilaptop-01.csv')
columns_to_keep = ['Event Time','Action Type', 'File Name', 'Folder Path', 'Sha1', 'Sha256','MD5', 'Account Name',\
                   'Initiating Process File Name', 'Initiating Process Folder Path','Process Command Line',\
                   'Process Id', 'Initiating Process Folder Path', 'Initiating Process Parent File Name', 'Remote Url', 'Remote IP', 'Remote IP',	'Remote Port',	'Local IP',	'Local Port',\
                   'File Origin Url',	'File Origin IP', 'File Origin Referrer Url', 'Categories','Severities']
df = df_base[columns_to_keep]
df.head()
#df.shape
#df.info()
