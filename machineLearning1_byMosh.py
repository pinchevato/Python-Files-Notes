# Tutorial has us do this in Jupyter notebook
# ..but it SUCKS FUCKING DICK n won't work >:(

# Import video game dataset
import pandas as pd
# create dataframe object
df = pd.read_csv('vgsales.csv')
print(df)
print(df.shape)
print(df.describe())



# IMPORT DATASET
import pandas as pd
mus_data = pd.read_csv('music.csv')
# Machine Learning Step #3: split into training & test sets
# input dataset
X = mus_data.drop(columns=['genre'])
# output dataset
y = mus_data['genre']
print(y.describe())

# CREATE MODEL (Learning & Predicting)
# ***sklearn only works in Jupyter..?
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
# TRAIN MODEL
model.fit(X, y)
# ASK MODEL TO MAKE PREDICTIONS
# Using sklearn, what would a 21 yo male like and what would a 22yo female like?
pred = model.predict([ [21,1], [22,0] ])
print(pred)
