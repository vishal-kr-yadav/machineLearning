# Load libraries
import pandas
#from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC



url="/home/vishal/Documents/iris.data";
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset=pandas.read_csv(url,names=names)
# Split-out validation dataset
array = dataset.values
X = array[:,0:4] #all value is stored
Y = array[:,4] #class name is stored
validation_size = 0.20
seed = 7
#sklearn.model_selection.train_test_split(*arrays, **options)[source]
#If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split.
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
scoring = 'accuracy'
# X_train and Y_train for preparing models and a X_validation and Y_validation sets that we can use later.
#print(Y_validation)
# Spot Check Algorithms

# # Make predictions on validation dataset
lr = LogisticRegression()
lr.fit(X_train, Y_train)
T_validation=[[7.0,3.2,4.7,1.4,]]
predictions = lr.predict(T_validation)
print(predictions)
