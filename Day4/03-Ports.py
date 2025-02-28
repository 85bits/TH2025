import pandas as pd
import json
df = pd.read_json('sample_data/Case85bitsGCP_gcp-goat.jsonl', lines=True)
#df = pd.read_json('sample_data/Case85bitsGCP_velvety.jsonl', lines=True)
json_payload_df = pd.json_normalize(df['jsonPayload'])
df = pd.concat([df, json_payload_df], axis=1)
df.drop('jsonPayload', axis=1, inplace=True) 
# Handle NaN values (if any)
df.dropna(subset=['connection.dest_port'], inplace=True)  # Or use fillna()
df['connection.dest_port'] = df['connection.dest_port'].astype(int)
print(df['connection.dest_port'].value_counts())
