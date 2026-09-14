import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



# 1. Create a simple house price dataset


data = {
    "Area": [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400,
             1500, 1600, 1700, 1800, 1900, 2000],
    
    "Price": [15, 18, 21, 24, 27, 30, 33, 36, 39, 42,
              45, 48, 51, 54, 57, 60]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# -------------------------------------------------
# 2. Check for missing values
# -------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# 3. Separate input and output


X = df[["Area"]]
y = df["Price"]



# 4. Split dataset into training and testing data


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -------------------------------------------------
# 5. Create Linear Regression model
# -------------------------------------------------

model = LinearRegression()



# 6. Train the model


model.fit(X_train, y_train)



# 7. Display coefficient and intercept


print("\nModel Coefficient:")
print(model.coef_[0])

print("\nModel Intercept:")
print(model.intercept_)


# -------------------------------------------------
# 8. Make predictions
# -------------------------------------------------

y_pred = model.predict(X_test)

print("\nActual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(y_pred)



# 9. Evaluate the model



mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error (MSE):")
print(mse)

print("\nR-squared (R2):")
print(r2)



# 10. Predict price for a new house


new_area = [[2500]]

predicted_price = model.predict(new_area)

print("\nPredicted price for 2500 sq.ft house:")
print(predicted_price[0])