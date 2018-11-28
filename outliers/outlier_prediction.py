import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("input_data.txt")
newdf = data[data['value'] != 0]

res = plt.boxplot(newdf['value'].tolist())

outlier= res["fliers"][0].get_data()[1]
print(outlier)
print(newdf['value'].describe())
plt.show()

# To delete outlier rows
outlier_data=(outlier.tolist())
for each in range(0,len(outlier_data)):
    data=data[data['value'] != outlier_data[each]]

print(data.to_csv("clean_data.csv",sep='\t'))
clean_data=pd.read_csv('clean_data.csv',sep='\t')
print(clean_data['value'].describe())