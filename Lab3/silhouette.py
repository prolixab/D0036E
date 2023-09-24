from kmeans import KMeans
import pandas as pd


class Silhouette:

    def __init__(self, df, centroids, x, y):
        self.df = df
        self.x = x
        self.y = y
        self.centroids = centroids

    def a(self, point_x, point_y, centroid):
        """
        Calculates a i.e. the average distance between point and all the other points in the cluster
        :param point_x:
        :param point_y:
        :param centroid: this is required to work out which points are in the same cluster
        :return:
        """
        distance_sum = 0
        df2 = self.df.where(self.df.centroid == centroid).dropna(how='all')
        for index, row in df2.iterrows():
            distance_sum += KMeans.calculate_euclidean(point_x, point_y, self.centroids[0][0], self.centroids[0][1])
        avg_distance = distance_sum / len(df2)
        return avg_distance

    def b(self, point_x, point_y, centroid):
        """
        Calculates distance between point and its next nearest cluster centroid
        :param point_x:
        :param point_y:
        :param centroid: this is needed to know which centroid is the next nearest..
        :return:
        """
        next_nearest = self.find_next_nearest_cluster_centroid(point_x, point_y, centroid)
        distance_sum = 0
        distance = KMeans.calculate_euclidean(point_x, point_y, self.centroids[next_nearest][0],
                                              self.centroids[next_nearest][1])
        return distance

    def calculate_sum_a(self, centroid):
        sum_a = 0
        df2 = self.df.where(self.df.centroid == centroid).dropna(how='all')
        for index, row in df2.iterrows():
            sum_a += self.a(row[self.x], row[self.y], centroid)
        return sum_a

    def find_next_nearest_cluster_centroid(self, point_x, point_y, centroid):

        results_df = pd.DataFrame()
        for index, c in enumerate(self.centroids):
            distance = KMeans.calculate_euclidean(point_x, point_y, self.centroids[0][0], self.centroids[0][1])
            new_row = {'centroid': centroid, 'distance': distance}
            results_df.append(new_row)
        results_df.sort_values("distance")
        return results_df.iloc[[1]]["centroid"]
