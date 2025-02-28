import pandas as pd
import json
df = pd.read_json('sample_data/Case85bitsGCP_gcp-goat.jsonl', lines=True)
json_payload_df = pd.json_normalize(df['jsonPayload'])
df = pd.concat([df, json_payload_df], axis=1)
df.drop('jsonPayload', axis=1, inplace=True) 
create_user_events = df[df['message'].str.contains("Creating user", na=False)]
pd.set_option('display.max_colwidth', None) 
print(create_user_events[['timestamp', 'operation',  'message']]) 
