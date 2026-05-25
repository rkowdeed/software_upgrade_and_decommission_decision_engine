# prompt: list me all java versions and their compatibility to all oracle versions in last 30 years in a tabular format

import pandas as pd

# Sample data (replace with actual data)
java_oracle_data = {
    'Java Version': ['Java 1.0', 'Java 1.1', 'Java 1.2', 'Java 5', 'Java 6', 'Java 7', 'Java 8', 'Java 9', 'Java 11', 'Java 17', 'Java 21'],
    'Oracle 7': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'Oracle 8': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'Oracle 8i': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'Oracle 9i': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'Oracle 10g': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'Oracle 11g': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'Oracle 12c': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'Oracle 18c': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible'],
    'Oracle 19c': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible'],
    'Oracle 21c': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible']

}

java_mysql_data = {
    'Java Version': ['Java 1.0', 'Java 1.1', 'Java 1.2', 'Java 5', 'Java 6', 'Java 7', 'Java 8', 'Java 9', 'Java 11', 'Java 17', 'Java 21'],
    'MySQL 3.23': ['Compatible', 'Compatible', 'Compatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'MySQL 4.0': ['Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'MySQL 4.1': ['Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'MySQL 5.0': ['Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'MySQL 5.1': ['Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'MySQL 5.5': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'MySQL 5.6': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'MySQL 5.7': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'MySQL 8.0': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
    'MySQL 8.1': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible']
}

java_dotnet_data = {
    'Java Version': ['Java 1.0', 'Java 1.1', 'Java 1.2', 'Java 5', 'Java 6', 'Java 7', 'Java 8', 'Java 9', 'Java 11',  'Java 17', 'Java 21'],
    '.NET 1.0': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible',  'Incompatible'],
    '.NET 1.1': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    '.NET 2.0': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    '.NET 3.0': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    '.NET 3.5': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible',  'Incompatible'],
    '.NET 4.0': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible',   'Compatible'],
    '.NET 4.5': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible',  'Compatible', 'Compatible', 'Compatible', 'Compatible',  'Compatible'],
    '.NET 4.6+': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible',  'Compatible'],    
    '.NET 5+': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible',  'Compatible']
}


java_python_data = {
     'Java Version': ['Java 1.0', 'Java 1.1', 'Java 1.2', 'Java 5', 'Java 6', 'Java 7', 'Java 8', 'Java 9', 'Java 11',  'Java 17', 'Java 21'],
    'Python 1.x': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'Python 1.x': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible'],
    'Python 3.x': ['Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Incompatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible', 'Compatible'],
}

df1 = pd.DataFrame(java_oracle_data)
df1
df2 = pd.DataFrame(java_mysql_data)
df2
df3 = pd.DataFrame(java_dotnet_data)
df3
df4 = pd.DataFrame(java_python_data)
df4



















