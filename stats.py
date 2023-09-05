import math


class StatFunctions:

    @staticmethod
    def min_function(input_list):
        min_value = input_list[0]
        for x in input_list:
            if x < min_value:
                min_value = x
        return min_value

    @staticmethod
    def max_function(input_list):
        max_value = input_list[0]
        for x in input_list:
            if x > max_value:
                max_value = x
        return max_value

    @staticmethod
    def mean_function(input_list):
        sum_value = 0
        for x in input_list:
            sum_value += x
        return sum_value / len(input_list)

    @staticmethod
    def variance_function(input_list):
        variance_sum = 0
        mean = StatFunctions.mean_function(input_list)
        for i in input_list:
            variance_sum += (i - mean) ** 2
        variance = variance_sum/len(input_list)
        return variance

    @staticmethod
    def std_function(input_list):
        std = math.sqrt(StatFunctions.variance_function(input_list))
        return std

    @staticmethod
    def median_function(input_list):
        # Check to see if this is the correct way for even number
        sorted_list = StatFunctions.bubble_sort(input_list)
        length = len(sorted_list)
        print(length)
        half_length = int(length / 2)
        print(half_length)
        if (length % 2) == 0:
            median_value = (sorted_list[half_length - 1] + sorted_list[half_length]) / 2.0
            return median_value
        else:
            return sorted_list[half_length]

    @staticmethod
    def mad_function(input_list):
        median = StatFunctions.median_function(input_list)
        absolute_deviations = []
        for i in input_list:
            absolute_deviation = abs(median - i)
            absolute_deviations.append(absolute_deviation)
        mad = StatFunctions.median_function(absolute_deviations)
        return mad

    @staticmethod
    def bubble_sort(input_list):
        list_copy = input_list.copy()
        for x in range(0, len(list_copy) - 1):
            pos = 0
            for y in range(pos, len(list_copy) - 1):
                if list_copy[y + 1] < list_copy[y]:
                    temp = list_copy[y]
                    list_copy[y] = list_copy[y + 1]
                    list_copy[y + 1] = temp
        return list_copy
