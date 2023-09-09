import matplotlib.pyplot as plt
import numpy as np



class LinearRegression:

    @staticmethod
    def calculate_linear_regression(df, x, y):
        """

        :param df: dataframe
        :param x: name of x value
        :param y: name of y value
        :return: a and b in y=ax+b
        """
        b = LinearRegression.calculate_b(df, x, y)
        a = LinearRegression.calculate_a(df, x, y, b)
        return a, b

    @staticmethod
    def add_predicted(df, x, y, a, b):
        """
        Adds a column of predicted values to dataset
        :param df: dataframe
        :param x: name of x column
        :param y: name of y column
        :param a: a in y=a+bx
        :param b: b in y=a + bx
        :return:
        """
        column_to_add = []
        for value in df[x]:
            column_to_add.append(a + value*b)
        df.loc[:, ["Predicted"]] = column_to_add
        return df

    @staticmethod
    def plot_linear_regression(df, x, y, a, b):
        plt.scatter(df[x], df[y], label='Data points')
        plt.plot(df[x], a + b * df[x], label='Regression')
        plt.xlabel("Age")
        plt.ylabel("Average Income")
        plt.title("Linear Regression")

        # Adding legend, which helps us recognize the curve according to it's color
        plt.legend()
        plt.show()

    @staticmethod
    def calculate_a(df, x, y, b):
        """

        :param df: dataframe
        :param x: name of x variable
        :param y: name of y variable
        :param b: value of b
        :return: a
        """
        sum_x = df[x].sum()
        sum_y = df[y].sum()
        n = len(df[y])
        a = (sum_y - (b * sum_x)) / n
        return a

    @staticmethod
    def calculate_b(df, x, y):
        """

        :param df: dataframe
        :param x: name of x variable
        :param y: name of y variable
        :return: b
        """
        sum_x = df[x].sum()
        sum_y = df[y].sum()
        xy = df[x] * df[y]
        xx = df[x] * df[x]
        sum_xy = xy.sum()
        sum_xx = xx.sum()
        n = len(df[y])

        top_row = n * sum_xy - (sum_x * sum_y)
        bottom_row = n * sum_xx - (sum_x ** 2)
        b = top_row / bottom_row

        return b

    @staticmethod
    def calculate_mse(df, y, y_pred):
        """

        :param y_pred: name of predicted y variable
        :param df: dataframe
        :param y: name of y variable
        :return: mean square error
        """
        mse_sum = 0
        n = len(df[y])
        y_hat = df[y].mean()
        for i,y_value in enumerate(df[y]):
            mse_sum += (y_value - df.loc[df.index[i]][y_pred]) ** 2
        mse = mse_sum / n
        return mse
