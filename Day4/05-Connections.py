import pandas as pd
import json
df = pd.read_json('sample_data/Case85bitsGCP_gcp-goat.jsonl', lines=True)
json_payload_df = pd.json_normalize(df['jsonPayload'])
df = pd.concat([df, json_payload_df], axis=1)
df.drop('jsonPayload', axis=1, inplace=True)
connection_counts = df.groupby(['connection.src_ip', 'connection.dest_ip']).size().reset_index(name='connection_count')
# Sort by connection_count in descending order and get the top 10
top_10_connections = connection_counts.sort_values(by='connection_count', ascending=False).head(10)
# Sort by connection_count in ascending order and get the top 10
bottom_10_connections = connection_counts.sort_values(by='connection_count', ascending=True).head(10)
# Display the top 10 and bottom 10 connections
print("Top 10 Connections:")
print(top_10_connections)
print("\nBottom 10 Connections:")
print(bottom_10_connections)
