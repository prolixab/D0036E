import math
import random

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

            self.centroids = calculate_all_centroids(self.df, self.x, self.y)
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


def calculate_all_centroids(df, x, y):
    df2 = df.groupby("centroid").agg({
                                            y: 'mean',
                                            x: 'mean',
                                            })
    centroids = []
    for index, row in df2.iterrows():
        centroids.append([row[x], row[y]])
    return centroids
