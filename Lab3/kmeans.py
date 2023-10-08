import math
import random
import pandas as pd
import matplotlib.pyplot as plt

from stats import StatFunctions


class KMeans:

    def __init__(self, df, x, y, k, no_iterations):
        self.df = df
        self.x = x
        self.y = y
        self.k = k
        self.no_iterations = no_iterations
        self.centroids = []

    def get_centroids(self):
        return self.centroids

    @staticmethod
    def calculate_euclidean(x1, y1, x2, y2):
        x_dist = x2 - x1
        y_dist = y2 - y1
        distance = math.sqrt(x_dist ** 2 + y_dist ** 2)
        return distance

    def kmeans(self):
        # Find min x, max x
        # Find min y, max y
        min_x = StatFunctions.min_function(self.df[self.x])
        min_y = StatFunctions.min_function(self.df[self.y])
        max_x = StatFunctions.max_function(self.df[self.x])
        max_y = StatFunctions.max_function(self.df[self.y])

        for x in range(self.k):
            x_point = random.uniform(min_x, max_x)
            y_point = random.uniform(min_y, max_y)
            self.centroids.append([x_point, y_point])

        # Assignment step - assign each point to nearest centroid
        print(self.centroids)
        for i in range(self.no_iterations):
            KMeans.assign_centroids(self.df, self.x, self.y, self.centroids)
            # print(self.df)

            self.centroids = self.calculate_all_centroids(self.df, self.x, self.y)
            print(self.centroids)

    @staticmethod
    def assign_centroids(df, x, y, centroids):
        # Assignment step - assign each point to nearest centroid
        centroid_array = []
        for index, row in df.iterrows():
            closest = KMeans.calculate_nearest_centroid([row[x], row[y]], centroids)
            centroid_array.append(closest)
        df["centroid"] = centroid_array
        return

    @staticmethod
    def calculate_nearest_centroid(point, centroid_list):
        """
        Calculates which centroid is closest to given point
        :param point: point as array
        :param centroid_list: list of centroids
        :return: position of centroid in centroid list
        """
        closet_centroid = -1
        closest_centroid_distance = -1.0
        for i, centroid in enumerate(centroid_list):
            distance = KMeans.calculate_euclidean(point[0], point[1], centroid[0], centroid[1])
            if closest_centroid_distance < 0 or distance < closest_centroid_distance:
                closest_centroid_distance = distance
                closet_centroid = i
        return closet_centroid

    @staticmethod
    def find_center_point(x_point_list, y_point_list):
        x_sum = 0
        y_sum = 0
        x_len = len(x_point_list)
        y_len = len(y_point_list)
        for i in range(x_len):
            x_sum += x_point_list[i]
            y_sum += y_point_list[i]

        x_center = x_sum / x_len
        y_center = y_sum / y_len
        return [x_center, y_center]

    @staticmethod
    def calculate_all_centroids(df, x, y):
        df2 = df.groupby("centroid").agg({
            y: 'mean',
            x: 'mean',
        })
        centroids = []
        for index, row in df2.iterrows():
            centroids.append([row[x], row[y]])
        return centroids

    def graph_results(self):
        plt.scatter(self.df[self.x], self.df[self.y], c=self.df["centroid"])
        xs = [x[0] for x in self.centroids]
        ys = [x[1] for x in self.centroids]
        plt.scatter(xs, ys, marker="x")
        plt.show()

    # Silhouette score

    def calculate_average_s(self):
        s_sum = 0
        for index, row in self.df.iterrows():
            s = self.calculate_single_s(row[self.x], row[self.y], row["centroid"])
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
        if distance_sum == 0:
            return 0
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

    def find_next_nearest_cluster_centroid(self, point_x, point_y, centroid):
        # Deal with only one centroid
        if len(self.centroids) == 1:
            return 0
        results_df = pd.DataFrame(columns=["centroid", "distance"])
        for index, c in enumerate(self.centroids):
            distance = KMeans.calculate_euclidean(point_x, point_y, self.centroids[index][0], self.centroids[index][1])
            new_row = pd.DataFrame({'centroid': [index], 'distance': [distance]})
            results_df = pd.concat([results_df, new_row], ignore_index=True)
        results_df = results_df.sort_values("distance")
        return results_df.iloc[1]["centroid"]
