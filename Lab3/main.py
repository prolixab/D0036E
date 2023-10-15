from io_functions import IOFunctions
import matplotlib.pyplot as plt
from kmeans import KMeans
import numpy as np

# 1.1
df = IOFunctions.read_file_to_dataframe("inc_vs_rent.csv")
print(df.head(10))

# 1.2
plt.scatter(df["Annual rent sqm"], df["Avg yearly inc KSEK"])
plt.xlabel("Annual rent sqm")
plt.ylabel("Avg yearly inc KSEK")
plt.title("Rent vs. Income")
plt.tight_layout()
plt.show()

# 1.3
km = KMeans(df, "Annual rent sqm", "Avg yearly inc KSEK", 3, 10)
km.kmeans()
centroids = km.get_centroids()
df_with_centroids = km.df

plt.scatter(df_with_centroids["Annual rent sqm"], df_with_centroids["Avg yearly inc KSEK"],
            c=df_with_centroids["centroid"])
xs = [x[0] for x in centroids]
ys = [x[1] for x in centroids]
plt.scatter(xs, ys, marker="x")
plt.xlabel("Annual rent sqm")
plt.ylabel("Avg yearly inc KSEK")
plt.title("Rent vs. Income with centroids shown")
plt.tight_layout()
plt.show()

# 2.1
# Grid search implementation
hyperparameter_list = []
k_list = []
result_list = []
for x in range(1, 10, 1):
    hyperparameter_list.append(x)
    km = KMeans(df, "Annual rent sqm", "Avg yearly inc KSEK", x, 10)
    km.kmeans()
    k_list.append(km)
    result = km.calculate_average_s()
    result_list.append(result)

ind = np.argmax(result_list)
print(f"Silhouette scores: {result_list}")
print(f"Index of max: {ind}")
best_km = k_list[ind]
print(f"Optimal number of k is {best_km.k}")

# 2.2
# Graphing hyperparameter against S Score
plt.scatter(hyperparameter_list, result_list)
plt.xlabel("k")
plt.ylabel("S score")
plt.title("k vs. S score for KMeans.")
plt.show()

# Graphing K_means with best k
best_km.graph_results()

# 2.3 [ 1010, 320.12], [1258, 320], [980, 292.4]
no1 = best_km.predict(1010, 320.12)
no2 = best_km.predict(1258, 320)
no3 = best_km.predict(980, 292.4)
print(f"Predicted centroids: {no1} {no2}  {no3}")
df = best_km.df
centroids = best_km.get_centroids()

plt.scatter(best_km.df["Annual rent sqm"], best_km.df["Avg yearly inc KSEK"], c=best_km.df["centroid"])
for index, row in df.iterrows():
    plt.text(row["Annual rent sqm"], row["Avg yearly inc KSEK"],str(row["centroid"]))
xs = [x[0] for x in centroids]
ys = [x[1] for x in centroids]
plt.scatter(xs, ys, marker="x")
plt.text(1010, 320.12, str(no1) )
plt.text(1258, 320, str(no2) )
plt.text(980, 292.4, str(no3) )
plt.scatter(1010, 320.12, marker="P")
plt.scatter(1258, 320, marker="P")
plt.scatter(980, 292.4, marker="X")
plt.xlabel("Annual rent sqm")
plt.ylabel("Avg yearly inc KSEK")
plt.title("Rent vs. Income with predicted centroids shown")

plt.tight_layout()
plt.show()

print("Finished")
