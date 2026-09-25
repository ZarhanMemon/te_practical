# PR10: PCA

import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. Load dataset
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Original Number of Features:", X.shape[1])


# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 3. Standardization
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# --------------------------------
# 4. Classification BEFORE PCA
# --------------------------------

model_before = LogisticRegression(max_iter=1000)

model_before.fit(X_train_scaled, y_train)

y_pred_before = model_before.predict(X_test_scaled)

accuracy_before = accuracy_score(
    y_test,
    y_pred_before
)

print("\nAccuracy Before PCA:", accuracy_before)


# --------------------------------
# 5. Apply PCA
# --------------------------------

pca = PCA(n_components=2)

X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

print("Number of Features After PCA:", X_train_pca.shape[1])


# --------------------------------
# 6. Classification AFTER PCA
# --------------------------------

model_after = LogisticRegression()

model_after.fit(X_train_pca, y_train)

y_pred_after = model_after.predict(X_test_pca)

accuracy_after = accuracy_score(
    y_test,
    y_pred_after
)

print("Accuracy After PCA:", accuracy_after)




# --------------------------------
# 7. Comparison
# --------------------------------

print("\nComparison")
print("Features Before PCA:", X.shape[1])
print("Features After PCA :", X_train_pca.shape[1])
print("Accuracy Before PCA:", accuracy_before)
print("Accuracy After PCA :", accuracy_after)




Output:-

Original Number of Features: 30

Accuracy Before PCA: 0.9736842105263158
Number of Features After PCA: 2
Accuracy After PCA: 0.9912280701754386

Comparison
Features Before PCA: 30
Features After PCA : 2
Accuracy Before PCA: 0.9736842105263158
Accuracy After PCA : 0.9912280701754386
PS C:\Practical> 