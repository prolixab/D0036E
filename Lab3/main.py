from io_functions import IOFunctions
import matplotlib.pyplot as plt
from kmeans import KMeans
from silhouette import Silhouette
from gridsearch import GridSearch
import numpy as np

# 1.1
df = IOFunctions.read_file_to_dataframe("inc_vs_rent.csv")
print(df.head(10))

# 1.2
plt.scatter(df["Annual rent sqm"], df["Avg yearly inc KSEK"])
plt.show()

# 1.3
km = KMeans(df, "Annual rent sqm", "Avg yearly inc KSEK", 3, 10)
km.kmeans()
centroids = km.get_centroids()

plt.scatter(df["Annual rent sqm"], df["Avg yearly inc KSEK"], c=df["centroid"])
xs = [x[0] for x in centroids]
ys = [x[1] for x in centroids]
plt.scatter(xs, ys, marker="x")
plt.show()

# 2.1
#sm = Silhouette(df, km.get_centroids(), "Annual rent sqm", "Avg yearly inc KSEK")
avgs=km.calculate_average_s()

# ??
hyperparameter_list = []
k_list=[]
result_list = []
for x in range(1, 10, 1):
    hyperparameter_list.append(x)
    km = KMeans(df, "Annual rent sqm", "Avg yearly inc KSEK", x, 10)
    km.kmeans()
    result = km.calculate_average_s()
    k_list.append(km)
    result_list.append(result)
#gs = GridSearch(1,10, 1)

ind = np.argmax(result_list)
print(ind)
print(result_list)
# avg_dist=sm.a(5,10,0)
# print(avg_dist)
