from kmeans import KMeans
import pandas as pd


class Silhouette:

    def __init__(self, df, centroids, x_name, y_name):
        self.df = df
        self.x_name = x_name
        self.y_name = y_name
        self.centroids = centroids

    def calculate_average_s(self):
        s_sum = 0
        for index, row in self.df.iterrows():
            s = self.calculate_single_s(row[self.x_name], row[self.y_name], row["centroid"])
            s_sum += s
        average_s = s_sum / len(self.df)
        return average_s

    def calculate_single_s(self, point_x, point_y, centroid):
        a = self.a(point_x, point_y, centroid)
        b = self.b(point_x, point_y, centroid)
        max_no = max(a, b)
        s = (b - a) / max_no
        return s

    def a(self, point_x, point_y, centroid):
        """
        Calculates a i.e. the average distance between point and all the other points in the cluster
        :param point_x:
        :param point_y:
        :param centroid: position of centroid in centroid list, this is required to work out which points are in the same cluster
        :return:
        """
        distance_sum = 0
        # Drop all points which belong to other centroids
        df2 = self.df.where(self.df.centroid == centroid).dropna(how='all')
        for index, row in df2.iterrows():
            distance_sum += KMeans.calculate_euclidean(point_x, point_y, self.centroids[centroid][0],
                                                       self.centroids[centroid][1])
        # Calculate average - note -1 to deal with counting the point itself.
        avg_distance = distance_sum / (len(df2) - 1)
        return avg_distance

    def b(self, point_x, point_y, centroid):
        """
        Calculates distance between point and its next nearest cluster centroid
        TODO this should be average distance to points.
        :param point_x:
        :param point_y:
        :param centroid: this is needed to know which centroid is the next nearest..
        :return:
        """
        next_nearest = self.find_next_nearest_cluster_centroid(point_x, point_y, centroid)
        distance_sum = 0
        df2 = self.df.where(self.df.centroid == next_nearest).dropna(how='all')
        for index, row in df2.iterrows():
            distance_sum += KMeans.calculate_euclidean(point_x, point_y, self.centroids[next_nearest][0],
                                                       self.centroids[next_nearest][1])
        avg_distance = distance_sum / len(df2)
        return avg_distance

    # def calculate_sum_a(self, centroid):
    #     sum_a = 0
    #     df2 = self.df.where(self.df.centroid == centroid).dropna(how='all')
    #     for index, row in df2.iterrows():
    #         sum_a += self.a(row[self.x], row[self.y], centroid)
    #     return sum_a

    def find_next_nearest_cluster_centroid(self, point_x, point_y, centroid):
        results_df = pd.DataFrame(columns=["centroid", "distance"])
        for index, c in enumerate(self.centroids):
            distance = KMeans.calculate_euclidean(point_x, point_y, self.centroids[index][0], self.centroids[index][1])
            new_row = pd.DataFrame({'centroid': [index], 'distance': [distance]})
            results_df = pd.concat([results_df, new_row], ignore_index=True)
        results_df=results_df.sort_values("distance")
        return results_df.iloc[1]["centroid"]
