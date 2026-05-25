import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_jdk_versions():
    # URL of the OpenJDK release page
    url = "https://jdk.java.net/archive/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract version and release date information
    versions = []
    for a in soup.find_all('a', href=True):
        link_text = a.text.strip()
        if link_text.startswith('JDK'):
            versions.append(link_text)

    return versions

def create_dataframe(versions):
    data = []
    for version in versions:
        # Split to get version number and release date
        parts = version.split()
        version_number = parts[0].replace('JDK', '').strip()
        release_date = parts[1].strip() if len(parts) > 1 else 'Unknown'
        data.append([version_number, release_date])

    df = pd.DataFrame(data, columns=['Version', 'Release Date'])
    return df

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

# Fetch JDK versions
jdk_versions = fetch_jdk_versions()

# Create DataFrame
jdk_df = create_dataframe(jdk_versions)

# Save to CSV
save_to_csv(jdk_df, 'jdk_versions.csv')

print(jdk_df)
