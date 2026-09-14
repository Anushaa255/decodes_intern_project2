import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score


# 1. Create dataset
data = {
    "Height": [150, 155, 160, 165, 170, 175, 180, 185, 190, 195],
    "Weight": [45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
    "Class": [
        "Underweight",
        "Underweight",
        "Underweight",
        "Normal",
        "Normal",
        "Normal",
        "Overweight",
        "Overweight",
        "Overweight",
        "Overweight"
    ]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. Separate features and target
X = df[["Height", "Weight"]]
y = df["Class"]


# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)


# 4. Try different K values
for k in [1, 3, 5]:

    print("\n-----------------------------")
    print("K =", k)
    print("-----------------------------")

    # Create KNN model
    model = KNeighborsClassifier(n_neighbors=k)

    # Train model
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test, y_pred, average="weighted", zero_division=0
    )
    recall = recall_score(
        y_test, y_pred, average="weighted", zero_division=0
    )

    print("Actual Values:")
    print(y_test.values)

    print("Predicted Values:")
    print(y_pred)

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))


# 5. Predict a new data point
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

new_data = [[172, 68]]

prediction = model.predict(new_data)

print("\nNew Data:")
print("Height = 172 cm")
print("Weight = 68 kg")
print("Predicted Class:", prediction[0])