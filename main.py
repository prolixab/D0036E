from io_functions import IOFunctions
from stats import StatFunctions
import seaborn as sns
import matplotlib.pyplot as plt

csv_filename = "housing.csv"

# Task 1 - See stats.py
grades = [8, 6, 1, 7, 8, 9, 8, 7, 10, 7, 6, 9, 7]

# Task 2
min_value = StatFunctions.min_function(grades)
max_value = StatFunctions.max_function(grades)
mean = StatFunctions.mean_function(grades)
std = StatFunctions.std_function(grades)
variance = StatFunctions.variance_function(grades)
median = StatFunctions.median_function(grades)
MAD = StatFunctions.mad_function(grades)

print(f"Grades array: {grades}")
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
print(f"Mean value (sum/n): {mean}")
print(f"STD (root of variance): {std}")
print(f"Variance ( mean of square of distance from population mean: {variance}")
print(f"Median (midpoint of ordered list): {median}")
print(f"MAD (median of absolute deviations from median: {MAD}")

# Task 3
df = IOFunctions.read_file_to_dataframe(csv_filename)
print(df.head(10))

# Task 4

print(f"4.1: Number of rows:{len(df)}")
print(f"4.2: Mean:{StatFunctions.mean_function(df['median_house_value']):.2f}")
fig, axs = plt.subplots(ncols=2, nrows=2)
sns.set()
sns.histplot(data=df, x="households", ax=axs[0, 0])
sns.histplot(data=df, x="median_income", ax=axs[0, 1])
sns.histplot(data=df, x="housing_median_age", ax=axs[1, 0])
sns.histplot(data=df, x="median_house_value", ax=axs[1, 1])
plt.show()

#4.4: In general not normally distributed
#4.4 Housing_median_age : Again, not normally distributed.
#4.4 Median_house_value: Skewered to one side and an abnormal number of high value houses.

#4.5 Have they been normalised to between 0 and 500000?

# Additional Task
df_by_op = df.groupby('ocean_proximity')['median_house_value'].mean()
print(df_by_op.head(10))

# 4.6
# 1: Mean and SD are best for this.
# 2: Median, to prevent outliers from affecting figures too much.