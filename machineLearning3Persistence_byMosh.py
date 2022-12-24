import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# joblib object has methods for saving n loading models
##from sklearn.externals import joblib
# ^^ this is what Mosh said, but things have changed:
import joblib

mus_data = pd.read_csv('music.csv')
X = mus_data.drop(columns=['genre'])
y = mus_data['genre']

model = DecisionTreeClassifier()
model.fit(X,y)

# This gives us a binary file that represents our model
joblib.dump(model, 'music-recommender.joblib')


# Once this file is saved, use the following to make predicitons
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
joblib.load('music-recommender.joblib')
predictions = model.predict([[21,1]])
