# PR7: Logistic Regression and KNN

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# 1. Load dataset
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Dataset loaded successfully")
print("Dataset Shape:", X.shape)


# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 3. Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# --------------------------------
# 4. Logistic Regression
# --------------------------------

logistic_model = LogisticRegression()

logistic_model.fit(X_train, y_train)

y_pred_logistic = logistic_model.predict(X_test)


# Evaluation
accuracy_lr = accuracy_score(y_test, y_pred_logistic)
precision_lr = precision_score(y_test, y_pred_logistic)
recall_lr = recall_score(y_test, y_pred_logistic)
f1_lr = f1_score(y_test, y_pred_logistic)

print("\nLogistic Regression Results")
print("Accuracy :", accuracy_lr)
print("Precision:", precision_lr)
print("Recall   :", recall_lr)
print("F1 Score :", f1_lr)


# Confusion Matrix
cm_lr = confusion_matrix(y_test, y_pred_logistic)

print("\nLogistic Regression Confusion Matrix:")
print(cm_lr)


# --------------------------------
# 5. KNN
# --------------------------------

knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train, y_train)

y_pred_knn = knn_model.predict(X_test)


# Evaluation
accuracy_knn = accuracy_score(y_test, y_pred_knn)
precision_knn = precision_score(y_test, y_pred_knn)
recall_knn = recall_score(y_test, y_pred_knn)
f1_knn = f1_score(y_test, y_pred_knn)

print("\nKNN Results")
print("Accuracy :", accuracy_knn)
print("Precision:", precision_knn)
print("Recall   :", recall_knn)
print("F1 Score :", f1_knn)


# Confusion Matrix
cm_knn = confusion_matrix(y_test, y_pred_knn)

print("\nKNN Confusion Matrix:")
print(cm_knn)


# --------------------------------
# 6. Compare Results
# --------------------------------

results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "KNN"
    ],
    "Accuracy": [
        accuracy_lr,
        accuracy_knn
    ],
    "Precision": [
        precision_lr,
        precision_knn
    ],
    "Recall": [
        recall_lr,
        recall_knn
    ],
    "F1 Score": [
        f1_lr,
        f1_knn
    ]
})

print("\nComparison of Results:")
print(results)


# --------------------------------
# 7. Display Confusion Matrices
# --------------------------------

plt.figure(figsize=(5, 4))
sns.heatmap(cm_lr, annot=True, fmt="d")
plt.title("Logistic Regression Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


plt.figure(figsize=(5, 4))
sns.heatmap(cm_knn, annot=True, fmt="d")
plt.title("KNN Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


Output:-

PS C:\Practical\AIML> py exp_7.py
Dataset loaded successfully
Dataset Shape: (569, 30)

Logistic Regression Results
Accuracy : 0.9736842105263158
Precision: 0.9722222222222222
Recall   : 0.9859154929577465
F1 Score : 0.9790209790209791

Logistic Regression Confusion Matrix:
[[41  2]
 [ 1 70]]

KNN Results
Accuracy : 0.9473684210526315
Precision: 0.9577464788732394
Recall   : 0.9577464788732394
F1 Score : 0.9577464788732394

KNN Confusion Matrix:
[[40  3]
 [ 3 68]]

Comparison of Results:
                 Model  Accuracy  Precision    Recall  F1 Score
0  Logistic Regression  0.973684   0.972222  0.985915  0.979021
1                  KNN  0.947368   0.957746  0.957746  0.957746
PS C:\Practical\AIML> 
