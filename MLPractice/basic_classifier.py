from sklearn import tree

import numpy as np


X = [[65,9],[67,7],[70,11],[62,6],[60,7],[72,13],[66,10],[67,7.5]]

Y=["male","female","male","female","female","male","male","female"]

clf = tree.DecisionTreeClassifier()

clf.fit(X, Y)

prediction = clf.predict([62,7])

print(prediction)

