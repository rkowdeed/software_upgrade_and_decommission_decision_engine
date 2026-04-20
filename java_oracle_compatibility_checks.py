# prompt: list me all java versions and their compatibility to all oracle versions in last 30 years in a tabular format

import pandas as pd

# Sample data (replace with actual data)
data = {
    'Java Version': ['Java 1.0', 'Java 1.1', 'Java 1.2', 'Java 5', 'Java 6', 'Java 7', 'Java 8', 'Java 9', 'Java 11', 'Java 17', 'Java 21'],
    'Oracle 7': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'Oracle 8': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'Oracle 8i': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'Oracle 9i': ['Incompatible', 'Incompatible', 'Partial', 'Partial', 'Partial', 'Partial', 'Partial', 'Partial', 'Partial', 'Partial', 'Partial'],
    'Oracle 10g': ['Incompatible', 'Incompatible', 'Incompatible', 'Partial', 'Partial', 'Partial', 'Full', 'Full', 'Full', 'Full', 'Full'],
    'Oracle 11g': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Partial', 'Partial', 'Full', 'Full', 'Full', 'Full', 'Full'],
    'Oracle 12c': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Partial', 'Full', 'Full', 'Full', 'Full', 'Full'],
    'Oracle 18c': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Partial', 'Partial', 'Full', 'Full', 'Full'],
    'Oracle 19c': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Partial', 'Full', 'Full', 'Full'],
    'Oracle 21c': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Partial', 'Full', 'Full']

}

df = pd.DataFrame(data)
df