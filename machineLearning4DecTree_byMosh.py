# Visualizing a decision tree
# THIS WILL NOT WORK UNLESS YOU USE VSCODE
# INSTEAD OF IDLE OR SOME SHIT..
# CAN'T INSTALL GRAPHVIZ DOT EXTENSION. FUCK.
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

mus_data = pd.read_csv('music.csv')
X = mus_data.drop(columns=['genre'])
y = mus_data['genre']

model = DecisionTreeClassifier()
model.fit(X, y)

tree.export_graphviz(model, out_file = 'music-recommender.dot',
                     feature_names=['age', 'gender'],
                     class_names=sorted(y.unique()),
                     label = 'all',
                     rounded=True,
                     filled=True,)
