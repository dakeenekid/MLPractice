#Used to determine men from women based on height and shoe size

from sklearn import tree

#height and shoe size
X = [[65,9],[67,7],[70,11],[62,6],[60,7],[72,13],[66,10],[67,7.5]]

Y=["male","female","male","female","female","male","male","female"]

#creating a decision tree
clf = tree.DecisionTreeClassifier()

#fitting the data to the tree
clf.fit(X, Y)

#predicting the gender based on a prediction
prediction = clf.predict([62,7])

#print the predicted gender
print(prediction)

