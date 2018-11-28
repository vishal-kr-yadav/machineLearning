import pandas as pd
import matplotlib.pyplot as plt

data={"X":[1,2,4,3,5],"Y":[1,3,3,2,5]}
dataset=pd.DataFrame(data)

# it will return the intercept(Bo) & slope(B1)
def co_efficient(x,y,x_mean,y_mean):
    temp_a=0
    temp_b=0
    for each_x,each_y in zip(x,y):
        temp_a+=(each_x-x_mean)*(each_y-y_mean)
        temp_b+=(each_x-x_mean)**2
    # print(a,b)
    B1=temp_a/temp_b
    Bo=y_mean-B1*x_mean
    return Bo,B1



X_mean=dataset["X"].mean()
Y_mean=dataset["Y"].mean()
Bo,B1=co_efficient(dataset["X"],dataset["Y"],X_mean,Y_mean)
# print(Bo,B1)

def pred(x,l,Bo,B1):
    for each in x:
        l.append(Bo+B1*each)
    return l,x


predicted_value,x_value=pred(dataset["X"],[],Bo,B1)
print("predicted_value=",predicted_value)

plt.plot(dataset["X"],dataset["Y"],'ro')
plt.plot(predicted_value,x_value,'bo')
plt.plot(predicted_value,x_value,'g')
plt.grid(True)
plt.axis([0, 6, 0, 6])
plt.show()

print(float(len(dataset['Y'])))
def rmse(predicted_value,y_value):
    temp_c=(float(len(y_value)))
    a=0
    for each_pred,y_value in zip(predicted_value,y_value):
       a+=(each_pred-y_value)**2
    return (a/temp_c)**0.5

a=rmse(predicted_value,dataset['Y'])
print(a)

# https://machinelearningmastery.com/simple-linear-regression-tutorial-for-machine-learning/

