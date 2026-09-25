# PR11: Advanced Machine Learning and Model Optimization

import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV
)

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

from sklearn.metrics import accuracy_score


# 1. Load dataset
data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Dataset Shape:", X.shape)


# 2. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 3. Models Before Optimization
# ==========================================

svm_model = make_pipeline(
    StandardScaler(),
    SVC()
)

rf_model = RandomForestClassifier(
    random_state=42
)

ada_model = AdaBoostClassifier(
    random_state=42
)


# Train models
svm_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)
ada_model.fit(X_train, y_train)


# Predictions
svm_pred = svm_model.predict(X_test)
rf_pred = rf_model.predict(X_test)
ada_pred = ada_model.predict(X_test)


# Accuracy
svm_accuracy = accuracy_score(y_test, svm_pred)
rf_accuracy = accuracy_score(y_test, rf_pred)
ada_accuracy = accuracy_score(y_test, ada_pred)


print("\nAccuracy Before Optimization")
print("SVM         :", svm_accuracy)
print("Random Forest:", rf_accuracy)
print("AdaBoost    :", ada_accuracy)


# ==========================================
# 4. Cross Validation
# ==========================================

svm_cv = cross_val_score(
    svm_model,
    X,
    y,
    cv=5
)

rf_cv = cross_val_score(
    rf_model,
    X,
    y,
    cv=5
)

ada_cv = cross_val_score(
    ada_model,
    X,
    y,
    cv=5
)


print("\nCross Validation Scores")
print("SVM Average CV Score         :", svm_cv.mean())
print("Random Forest Average Score  :", rf_cv.mean())
print("AdaBoost Average CV Score    :", ada_cv.mean())


# ==========================================
# 5. Grid Search - SVM
# ==========================================

svm_parameters = {
    "svc__C": [0.1, 1, 10],
    "svc__kernel": ["linear", "rbf"]
}

svm_grid = GridSearchCV(
    svm_model,
    svm_parameters,
    cv=5
)

svm_grid.fit(X_train, y_train)

print("\nBest SVM Parameters:")
print(svm_grid.best_params_)


# ==========================================
# 6. Grid Search - Random Forest
# ==========================================

rf_parameters = {
    "n_estimators": [50, 100],
    "max_depth": [None, 5, 10]
}

rf_grid = GridSearchCV(
    rf_model,
    rf_parameters,
    cv=5
)

rf_grid.fit(X_train, y_train)

print("\nBest Random Forest Parameters:")
print(rf_grid.best_params_)


# ==========================================
# 7. Grid Search - AdaBoost
# ==========================================

ada_parameters = {
    "n_estimators": [50, 100],
    "learning_rate": [0.5, 1.0]
}

ada_grid = GridSearchCV(
    ada_model,
    ada_parameters,
    cv=5
)

ada_grid.fit(X_train, y_train)

print("\nBest AdaBoost Parameters:")
print(ada_grid.best_params_)


# ==========================================
# 8. Optimized Model Accuracy
# ==========================================

svm_best_pred = svm_grid.predict(X_test)
rf_best_pred = rf_grid.predict(X_test)
ada_best_pred = ada_grid.predict(X_test)


svm_best_accuracy = accuracy_score(
    y_test,
    svm_best_pred
)

rf_best_accuracy = accuracy_score(
    y_test,
    rf_best_pred
)

ada_best_accuracy = accuracy_score(
    y_test,
    ada_best_pred
)


print("\nAccuracy After Optimization")

print("SVM         :", svm_best_accuracy)
print("Random Forest:", rf_best_accuracy)
print("AdaBoost    :", ada_best_accuracy)


# ==========================================
# 9. Final Comparison
# ==========================================

results = pd.DataFrame({
    "Model": [
        "SVM",
        "Random Forest",
        "AdaBoost"
    ],
    "Before Optimization": [
        svm_accuracy,
        rf_accuracy,
        ada_accuracy
    ],
    "After Optimization": [
        svm_best_accuracy,
        rf_best_accuracy,
        ada_best_accuracy
    ]
})

print("\nFinal Comparison:")
print(results)



Output:-
PS C:\Practical\AIML> py exp_11_svm_randomforest.py
Dataset Shape: (569, 30)

Accuracy Before Optimization
SVM         : 0.9824561403508771
Random Forest: 0.9649122807017544
AdaBoost    : 0.9649122807017544

Cross Validation Scores
SVM Average CV Score         : 0.9736376339077782
Random Forest Average Score  : 0.9560937742586555
AdaBoost Average CV Score    : 0.9683744760130415

Best SVM Parameters:
{'svc__C': 0.1, 'svc__kernel': 'linear'}

Best Random Forest Parameters:
{'max_depth': 5, 'n_estimators': 100}

Best AdaBoost Parameters:
{'learning_rate': 1.0, 'n_estimators': 50}

Accuracy After Optimization
SVM         : 0.9824561403508771
Random Forest: 0.9649122807017544
AdaBoost    : 0.9649122807017544

Final Comparison:
           Model  Before Optimization  After Optimization
0            SVM             0.982456            0.982456
1  Random Forest             0.964912            0.964912
2       AdaBoost             0.964912            0.964912
PS C:\Practical\AIML> 