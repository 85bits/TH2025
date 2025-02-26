import re
import pandas as pd

df_base = pd.read_csv('sample_data/batilaptop-01.csv')
columns_to_keep = ['Event Time', 'Action Type', 'File Name', 'Folder Path', 'Sha1', 'Sha256', 'MD5', 'Account Name',
                   'Initiating Process File Name', 'Initiating Process Folder Path', 'Process Command Line',
                   'Process Id', 'Initiating Process Folder Path', 'Initiating Process Parent File Name', 'Remote Url',
                   'Remote IP', 'Remote IP', 'Remote Port', 'Local IP', 'Local Port',
                   'File Origin Url', 'File Origin IP', 'File Origin Referrer Url', 'Categories', 'Severities']
df = df_base[columns_to_keep].copy()

# Function to extract root domain name from URL
def extract_root_domain(url):
    if pd.isna(url):
        return None  # Return None for NaN values
    try:
        # Regular expression to handle various URL formats and extract root domain
        domain = re.search(r'^(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9.-]+)\/?', str(url))
        if domain:
            domain_parts = domain.group(1).split('.')
            if len(domain_parts) >= 2:
                return '.'.join(domain_parts[-2:])  # Get the last two parts
            else:
                return domain_parts[0]  # Return the single part if only one exists
        else:
            return None  # Return None if no match found
    except TypeError:
        return None  # Handle potential TypeError if url is not a string

# Apply the function to the 'Remote Url' column
df.loc[:, 'Root Domain'] = df['Remote Url'].apply(extract_root_domain)

# Display the first few rows with the new column
print(df[['Remote Url', 'Root Domain']].head())

# Display value counts to see the most frequent root domains
print("\nTop Root Domains:")
print(df['Root Domain'].value_counts().head(50))
