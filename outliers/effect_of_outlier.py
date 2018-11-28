# This example show how an outlier can harm your algorithm
import statistics as stat

data_with_outlier=[3,6,8,9,4,5]
data_without_outlier=[3,6,101,9,4,5]

mean_of_data_with_outlier=stat.mean(data_with_outlier)
mean_of_data_without_outlier=stat.mean(data_without_outlier)
print("mean_of_data_with_outlier:",mean_of_data_with_outlier)
print("mean_of_data_without_outlier:",mean_of_data_without_outlier)

variance_of_data_with_outlier=stat.variance(data_with_outlier)
variance_of_data_without_outlier=stat.variance(data_without_outlier)
print("variance_of_data_with_outlier:",variance_of_data_with_outlier)
print("variance_of_data_without_outlier:",variance_of_data_without_outlier)

stdev_of_data_with_outlier=stat.stdev(data_with_outlier)
stdev_of_data_without_outlier=stat.stdev(data_without_outlier)
print("stdev_of_data_with_outlier:",stdev_of_data_with_outlier)
print("stdev_of_data_without_outlier:",stdev_of_data_without_outlier)