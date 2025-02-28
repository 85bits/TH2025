import pandas as pd
import json
df = pd.read_json('sample_data/Case85bitsGCP_gcp-goat.jsonl', lines=True)
json_payload_df = pd.json_normalize(df['jsonPayload'])
df = pd.concat([df, json_payload_df], axis=1)
df.drop('jsonPayload', axis=1, inplace=True)
bucket_events = df[df['resource'].apply(lambda x: x.get('type') == 'gcs_bucket')]
proto_payload_df = pd.json_normalize(bucket_events['protoPayload'])
proto_payload_df.head()
