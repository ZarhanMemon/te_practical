import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# 1. Load dataset
df = sns.load_dataset("titanic")

print("Dataset loaded successfully")
print("Original Shape:", df.shape)


# 2. Display first rows
print("\nFirst 5 rows:")
print(df.head())


# 3. Check data types
print("\nData Types:")
print(df.dtypes)


# 4. Remove duplicate rows
df = df.drop_duplicates()


# 5. Remove unnecessary columns
df = df.drop([ "class", "who", "adult_male", "deck",
                "embark_town", "alive", "alone"], axis=1)


# 6. Handle missing values
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

print("\nMissing Values:")
print(df.isnull().sum())



# 7. Encoding
df["sex"] = df["sex"].map({"male": 0, "female": 1})

df = pd.get_dummies(df, columns=["embarked"], dtype=int)

print("\nData after Encoding:")
print(df.head())



# 8. Statistical analysis
print("\nStatistical Analysis:")
print(df.describe())



# 9. Histogram - age
plt.figure(figsize=(7, 5))
plt.hist(df["age"], bins=20)
plt.xlabel("age")
plt.ylabel("Frequency")
plt.title("age Distribution")
plt.show()



# 10. Histogram - fare
plt.figure(figsize=(7, 5))
plt.hist(df["fare"], bins=20)
plt.xlabel("fare")
plt.ylabel("Frequency")
plt.title("fare Distribution")
plt.show()


# 11. Boxplot - age
plt.figure(figsize=(7, 5))
sns.boxplot(x=df["age"])
plt.title("Boxplot of age")
plt.show()


# 12. Boxplot - fare
plt.figure(figsize=(7, 5))
sns.boxplot(x=df["fare"])
plt.title("Boxplot of fare")
plt.show()



# 13. Separate features and target
X = df.drop("survived", axis=1)
y = df["survived"]



# 14. Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



# 15. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)


# 16. Display final result
print("\nFinal Result")
print("Training Data Shape:", X_train.shape)
print("Testing Data Shape :", X_test.shape)

print("\nData preprocessing and EDA completed successfully.")



