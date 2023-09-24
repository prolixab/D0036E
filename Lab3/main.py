from io_functions import IOFunctions
import matplotlib.pyplot as plt
from kmeans import KMeans

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
plt.scatter(df["Annual rent sqm"], df["Avg yearly inc KSEK"],c=df["centroid"])
xs = [x[0] for x in centroids]
ys = [x[1] for x in centroids]
plt.scatter(xs,ys,marker="x")
plt.show()
