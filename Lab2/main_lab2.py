import numpy as np

from io_functions import IOFunctions
from linear_regression import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression as LinearRegressionSK
from sklearn.linear_model import LinearRegression as LR
import pandas as pd

import matplotlib.pyplot as plt
# To test
from sklearn.metrics import mean_squared_error

subset_filename = "inc_subset.csv"
fullset_filename = "inc_utf.csv"
# Task 1

df = IOFunctions.read_file_to_dataframe(subset_filename)
print(df.head(10))

# Task 2

# 2.1
validation_proportion = 0.2

validation = df.sample(frac=validation_proportion, random_state=42)
train = df.drop(validation.index)
a, b = LinearRegression.calculate_linear_regression(train, "age", "2020")
print(f"Result: a={a} b={b}")

# 2.2
LinearRegression.plot_linear_regression(df, "age", "2020", a, b)

# 2.3
augment_df = LinearRegression.add_predicted(validation, "age", "2020", a, b)
print(augment_df.head(10))

# 2.4
mse = LinearRegression.calculate_mse(augment_df, "2020", "Predicted")
print(mse)

# mse_scikit = mean_squared_error(augment_df["2020"], augment_df["Predicted"])
# print(mse_scikit)
# 2.5
# MSE is hard to interpret and depends upon the scale of the expected y values.
# However, this MSE is not terrible.

# 3

df3 = IOFunctions.read_file_to_dataframe(fullset_filename)
print(df3.head(10))
# Deal with 100+
df3["age"] = df3["age"].apply(lambda x: "100 years" if x == "100+ years" else x)
df3["age"] = df3["age"].apply(lambda x: int(x.rsplit(' ', 1)[0]))
print(df3.head(10))

df3_grouped_by_age_group = df3.groupby(["age"], as_index=False)["2020"].mean()
print(df3_grouped_by_age_group.head(10))

# 3.2
validation = df3_grouped_by_age_group.sample(frac=validation_proportion, random_state=42)
train = df3_grouped_by_age_group.drop(validation.index)
a, b = LinearRegression.calculate_linear_regression(train, "age", "2020")
print(f"Result: a={a} b={b}")

# 3.3
LinearRegression.plot_linear_regression(df3_grouped_by_age_group, "age", "2020", a, b)

# 3.4
# Which dataset? Train, validation, test?
augment_df = LinearRegression.add_predicted(train, "age", "2020", a, b)
print(augment_df.head(10))

# 3.5
mse = LinearRegression.calculate_mse(augment_df, "2020", "Predicted")
print(mse)

# 3.6 Much higher MSE since this is a curve and not a simple linear.

# 4.1 Linear regression works well for linear graphs but not for curves.

# 4.2 The prediction needs to be a polynomial.

# 5.1
X = np.reshape(validation["age"].values, (-1, 1))
y = np.reshape(validation["2020"].values, (-1, 1))


def calculateRegressionAndMSE(x):
    # Why False?
    poly_features = PolynomialFeatures(degree=x, include_bias=False)
    X_poly = poly_features.fit_transform(X)
    lin_reg = LinearRegressionSK()
    lin_reg.fit(X_poly, y)
    y_lin_fit = lin_reg.predict(X_poly)
    df5 = pd.DataFrame(list(zip(X, y, y_lin_fit)), columns=["age", "2020", "predicted"])
    mse = LinearRegression.calculate_mse(df5, "2020", "predicted")
    print("MSE for poly:", x, ": ", mse)


# 5.2
calculateRegressionAndMSE(2)
calculateRegressionAndMSE(3)
calculateRegressionAndMSE(5)
calculateRegressionAndMSE(8)

# 5.3 ??

# 5.3  8 is best, since it results in the lowest MSE
poly_features = PolynomialFeatures(degree=8, include_bias=False)
X_poly = poly_features.fit_transform(X)
lin_reg = LinearRegressionSK()
lin_reg.fit(X_poly, y)
y_lin_fit = lin_reg.predict(X_poly)
df5 = pd.DataFrame(list(zip(X, y, y_lin_fit)), columns=["age", "2020", "predicted"])
mse = LinearRegression.calculate_mse(df5, "2020", "predicted")

# 5.4
# TODO Add linear,curve through points.
plt.scatter(X, y)
plt.scatter(X, y_lin_fit)
plt.tight_layout()
plt.show()
