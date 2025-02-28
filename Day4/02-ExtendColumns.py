import pandas as pd
import json
df = pd.read_json('sample_data/Case85bitsGCP_gcp-goat.jsonl', lines=True)
json_payload_df = pd.json_normalize(df['jsonPayload'])
json_payload_df.columns
