import re
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sample_data/01-sysmon_events.csv')
field_names = set()
for event_data in df['xml_data']:
    for match in re.finditer(r"<Data Name='(.*?)'>", event_data):
        field_names.add(match.group(1))
# Imprimimos los campos que están dentro de xml_data field names
print("Extracted field names from xml_data:")
for field_name in sorted(field_names):
    print(f"  * {field_name}")
