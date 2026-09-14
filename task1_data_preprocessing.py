# Task 1: Data Preprocessing for Machine Learning

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# ---------------------------------------------------
# STEP 1: Create a sample raw dataset
# ---------------------------------------------------

data = {
    "Age": [25, 30, None, 35, 40, 28, None, 45],
    "Salary": [25000, 40000, 35000, None, 60000, 30000, 50000, 70000],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", None, "Finance", "IT"
    ],
    "Experience": [1, 5, 3, 7, 10, 2, 6, 12],
    "Purchased": [0, 1, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())


# ---------------------------------------------------
# STEP 2: Separate features and target
# ---------------------------------------------------

X = df.drop("Purchased", axis=1)
y = df["Purchased"]


# ---------------------------------------------------
# STEP 3: Identify numerical and categorical columns
# ---------------------------------------------------

numerical_features = ["Age", "Salary", "Experience"]
categorical_features = ["Department"]


# ---------------------------------------------------
# STEP 4: Handle missing numerical data
# Mean strategy is used for numerical columns
# ---------------------------------------------------

numerical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])


# ---------------------------------------------------
# STEP 5: Handle categorical data
# Missing values are replaced by most frequent value
# Then One-Hot Encoding is applied
# ---------------------------------------------------

categorical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])


# ---------------------------------------------------
# STEP 6: Combine numerical and categorical processing
# ---------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_pipeline, numerical_features),
        ("cat", categorical_pipeline, categorical_features)
    ]
)


# ---------------------------------------------------
# STEP 7: Split data into training and testing sets
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# ---------------------------------------------------
# STEP 8: Apply preprocessing
# ---------------------------------------------------

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)


# ---------------------------------------------------
# STEP 9: Display results
# ---------------------------------------------------

print("\nTraining data shape:")
print(X_train.shape)

print("\nTesting data shape:")
print(X_test.shape)

print("\nProcessed Training Data:")
print(X_train_processed.toarray()
      if hasattr(X_train_processed, "toarray")
      else X_train_processed)

print("\nProcessed Testing Data:")
print(X_test_processed.toarray()
      if hasattr(X_test_processed, "toarray")
      else X_test_processed)

print("\nData preprocessing completed successfully!")