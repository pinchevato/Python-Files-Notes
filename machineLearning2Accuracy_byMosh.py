# FULL MACHINE LEARNING
# 70-80% of our data for training, and 20-30% for testing
# "Instead of passing only two samples for making predictions
# (like in prev simple example), we can pass the dataset
# we have for testing, we'll get the predictions, then
# we can compare these predictions with the actual values
# in the testset. Based on that, we can calculate the accuracy"

# (some of this code is from 1st example)
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# This function allows us to splits dataset into two
# sets: one for training, one for testing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

mus_data = pd.read_csv('music.csv')
X = mus_data.drop(columns=['genre'])
y = mus_data['genre']
# Allocating 20% of our data for testing, returns a tuple
# IMPORTANT: if we increase test size (say from 0.2 [20%]
# to 0.5 [50%]), our accuracy goes down
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
# To calculate accuracy simply compare 'predictions' with
# actual values we have in output set for testing, 'y_test'
# Accuracy_score() returns a value from 0-1 or 0% - 100%
score = accuracy_score(y_test, predictions)
score
# HOWEVER, each subsequent time we run this, we'll get
# a DIFFERENT SCORE, because every time we split our data
# into training n test sets (train_test_split), we'll have
# different datasets, bc the function randomly picks data
# for training n testing
