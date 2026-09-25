# PR9: Clustering Techniques

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering


# 1. Load dataset
df = pd.read_csv("Mall_Customers.csv")

print("Dataset loaded successfully")
print(df.head())


# 2. Select features
X = df[["Annual Income (k$)", "Spending Score (1-100)"]]


# 3. Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# --------------------------------
# 4. Elbow Method
# --------------------------------

wcss = []

for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    wcss.append(model.inertia_)


plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()


# --------------------------------
# 5. K-Means Clustering
# --------------------------------

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

df["KMeans_Cluster"] = clusters

print("\nK-Means Clusters:")
print(df[["Annual Income (k$)",
          "Spending Score (1-100)",
          "KMeans_Cluster"]].head())


# Visualize K-Means clusters
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=clusters
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("K-Means Clusters")
plt.show()


# --------------------------------
# 6. Dendrogram
# --------------------------------

linked = linkage(X_scaled, method="ward")

plt.figure(figsize=(10, 5))

dendrogram(linked)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Distance")
plt.show()


# --------------------------------
# 7. Hierarchical Clustering
# --------------------------------

hierarchical = AgglomerativeClustering(
    n_clusters=5,
    linkage="ward"
)

hierarchical_clusters = hierarchical.fit_predict(X_scaled)

df["Hierarchical_Cluster"] = hierarchical_clusters

print("\nHierarchical Clusters:")
print(df[[
    "Annual Income (k$)",
    "Spending Score (1-100)",
    "Hierarchical_Cluster"
]].head())

print("\nClustering completed successfully.")




Output:-

Dataset loaded successfully
   CustomerID  Genre  Age  Annual Income (k$)  Spending Score (1-100)
0           1   Male   19                  15                      39
1           2   Male   21                  15                      81
2           3   Male   20                  16                       6
3           4   Male   23                  16                      77
4           5   Male   31                  17                      40

K-Means Clusters:
   Annual Income (k$)  Spending Score (1-100)  KMeans_Cluster
0                  15                      39              4
1                  15                      81              1
2                  16                       6              3
3                  16                      77              1
4                  17                      40              4

Hierarchical Clusters:
   Annual Income (k$)  Spending Score (1-100)  Hierarchical_Cluster
0                  15                      39                    2
1                  15                      81                    4
2                  16                       6                    0
3                  16                      77                    4
4                  17                      40                    2

Clustering completed successfully.
