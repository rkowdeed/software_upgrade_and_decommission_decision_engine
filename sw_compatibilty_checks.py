# prompt: generate python code that applies time series, decision tree, support vector machine , random forest , xg gradient boost ml models to predict version compatibility based on java, oracle, mysql, python and .net version data in last 30 years

# Install necessary libraries
!pip install pandas scikit-learn xgboost mglearn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import mglearn # For visualization (optional)

# Generate synthetic data for demonstration (replace with your actual data)
import numpy as np

np.random.seed(42)
n_samples = 1000

java_versions = np.random.randint(1, 21, size=n_samples)
oracle_versions = np.random.randint(7, 21, size=n_samples)
mysql_versions = np.random.randint(4, 12, size=n_samples)
python_versions = np.random.randint(2, 4, size=n_samples)
dotnet_versions = np.random.randint(1, 7, size=n_samples)
compatibility = np.random.randint(0, 2, size=n_samples)  # 0: Incompatible, 1: Compatible


data = pd.DataFrame({
    'Java': java_versions,
    'Oracle': oracle_versions,
    'MySQL': mysql_versions,
    'Python': python_versions,
    'DotNet': dotnet_versions,
    'Compatibility': compatibility
})

#print(data)

# Separate features (X) and target (y)
X = data.drop('Compatibility', axis=1)
y = data['Compatibility']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize and train different models
models = {
    'Decision Tree': DecisionTreeClassifier(),
    'Support Vector Machine': SVC(),
    'Random Forest': RandomForestClassifier(),
    'XGBoost': XGBClassifier()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'{name} Accuracy: {accuracy}')

# Example prediction with a new set of versions
new_version = pd.DataFrame({'Java': [21], 'Oracle': [21], 'MySQL': [9], 'Python': [3], 'DotNet': [7]})
# Make sure the new_version dataframe has the same columns and data types as the training data
prediction = models['Random Forest'].predict(new_version)
print(f'Compatibility prediction for the new version: {prediction[0]}') # 0:Incompatible, 1:Compatible