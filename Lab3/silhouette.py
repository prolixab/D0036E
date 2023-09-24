from kmeans import KMeans
import pandas as pd

class Silhouette:

    def __init__(self, df, centroids, x, y):
        self.df = df
        self.x = x
        self.y = y
        self.centroids = centroids


    def a(self,point_x, point_y, centroid):
        distance_sum=0
        df2 = self.df.where(self.df.centroid==centroid).dropna(how='all')
        for index, row in df2.iterrows():
            distance_sum+=KMeans.calculate_euclidean(point_x, point_y, self.centroids[0][0], self.centroids[0][1])
        avg_distance=distance_sum/len(df2)
        return avg_distance

    def calculate_sum_a(self, df, centroid):
        sum=0
        df2 = self.df.where(self.df.centroid == centroid).dropna(how='all')
        for index, row in df2.iterrows():
            sum+=self.a(point_x, point_y, centroid)
        return sum

    def find_next_nearest_cluster_centroid(self, point_x,point_y,df,centroid):

        results_df=pd.DataFrame()
        for index, c in enumerator(self.centroids):
            distance=Kmeans.calculate_euclidean(point_x,point_y,self.centroids[0][0], self.centroids[0][1])
            new_row = {'centroid': centroid, 'distance': distance}
            results_df.append(new_row)
        results_df.sort_values("distance")
        return results_df.iloc[[1]]["centroid"]
