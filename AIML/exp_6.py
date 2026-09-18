# PR6: Regression Techniques

import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# 1. Load California Housing dataset
data = fetch_california_housing()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Dataset loaded successfully")
print("Dataset Shape:", X.shape)


# 2. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)



# ------------------------------------------------
# 3. Linear Regression
# ------------------------------------------------

linear_model = make_pipeline(
    StandardScaler(),
    LinearRegression()
)

linear_model.fit(X_train, y_train)

# Prediction
y_pred_linear = linear_model.predict(X_test)


# Calculate Linear Regression metrics
mse_linear = mean_squared_error(y_test, y_pred_linear)
mae_linear = mean_absolute_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)


print("\nLinear Regression Results")
print("MSE:", mse_linear)
print("MAE:", mae_linear)
print("R2 Score:", r2_linear)



# ------------------------------------------------
# 4. Polynomial Regression
# ------------------------------------------------

polynomial_model = make_pipeline(
    StandardScaler(),
    PolynomialFeatures(degree=2),  # quadratic nature
    LinearRegression()
)

polynomial_model.fit(X_train, y_train)

# Prediction
y_pred_poly = polynomial_model.predict(X_test)


# Calculate Polynomial Regression metrics
mse_poly = mean_squared_error(y_test, y_pred_poly)
mae_poly = mean_absolute_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)


print("\nPolynomial Regression Results")
print("MSE:", mse_poly)
print("MAE:", mae_poly)
print("R2 Score:", r2_poly)



# ------------------------------------------------
# 5. Compare Results
# ------------------------------------------------


results = pd.DataFrame({
    "Model": ["Linear Regression", "Polynomial Regression"],
    "MSE": [mse_linear, mse_poly],
    "MAE": [mae_linear, mae_poly],
    "R2 Score": [r2_linear, r2_poly]
})


print("\nComparison of Results:")
print(results)


