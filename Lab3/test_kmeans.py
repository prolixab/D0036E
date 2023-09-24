from kmeans import KMeans

point = [34.34, 24.24]
centroid_list_2_closest = [[1.34, 1.23], [3, 4], [30.2, 23.22]]
centroid_list_0_closest = [[30.2, 23.22], [1.34, 1.23], [3, 4]]


def test_calculate_nearest_centroid_1():
    closest = KMeans.calculate_nearest_centroid(point, centroid_list_2_closest)
    assert closest == 2


def test_calculate_nearest_centroid_2():
    closest = KMeans.calculate_nearest_centroid(point, centroid_list_0_closest)
    assert closest == 0


def test_find_center_point():
    center_point = KMeans.find_center_point([0, 0, 10, 10], [0, 10, 10, 0])
    assert center_point == [5, 5]
