# -*- coding: utf-8 -*-
"""Project 1 - Diabetes Prediction .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15tx4bSHLg7CdSzyPw1s1D_bFbinOTU7z

Importing The Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
"""Data Collection and analysis
PIMA Diabetes dataset

"""

#loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('diabetes.csv')


# printing the first  5 rows of the dataset
# diabetes_dataset.head()

# number of rows and columns in this dataset
# diabetes_dataset.shape

# getting the statistical measures in this dataset
# diabetes_dataset.describe()

# diabetes_dataset['Outcome'].value_counts()

"""0 --> Non-Diabetic
1 --> Diabetic

"""

# diabetes_dataset.groupby('Outcome').mean()

# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome',axis = 1)
Y = diabetes_dataset['Outcome']

# print(Y)

"""Data Standardization

"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

a = standardized_data
b = Y
# print(a)
# print(b)

"""Splitting the Traning & Test data """

X_train,X_test,Y_train,Y_test = train_test_split(a,b,test_size = 0.2,stratify = b,random_state =2)

# print(a.shape,X_train.shape,X_test.shape)

"""Training the Modal"""

classifier = svm.SVC(kernel='linear')

#training the support vector Machine Classifier
classifier.fit(X_train,Y_train)

"""Modal Evaluation

**Accuracy Score**
"""
pickle.dump(classifier,open('model.pkl','wb'))
y_pred = classifier.predict(X_test)
c_m = confusion_matrix(Y_test,y_pred)
acc = accuracy_score(Y_test,y_pred)
print(c_m)
print(acc)
# accuracy score on the training data
# X_train_prediction = classifier.predict(X_train)
# training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

# print("Accuracy score of the training data : ",training_data_accuracy)

#accuracy score on the test data
# X_test_prediction = classifier.predict(X_test)
# test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

# print("Accuracy score on the test data : ",test_data_accuracy)

"""Making a Predictive System"""

# input_data = (8,176,90,34,300,33.7,0.467,58)
# #changing the input_data to numpy array
# input_data_as_numpy_array = np.asarray(input_data)

# # reshape the array as we are predicating for one instance
# input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# #standardize the input data
# std_data = scaler.transform(input_data_reshaped)
# print(std_data)

# prediction = classifier.predict(std_data)
# print(prediction)

# if(prediction[0] == 0):
#   print("The person is not diabetic")
# else:
#   print("The person is diabetic")