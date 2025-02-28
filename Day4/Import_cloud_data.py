import pandas as pd
import json
df = pd.read_json('sample_data/Case85bitsGCP_gcp-goat.jsonl', lines=True)
df.head()
