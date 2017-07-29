#Basic neural net that I am making from scratch. This is a step up from base_classifier, for I am using neural nets. This net is going to predict the likelyhood of a person being either male or female, based on shoe size and height.
import numpy as np
import tensorflow
import pandas

#Creating datasets

#Each X entry is a person's shoe size followed by their height
#Each Y entry is a person's odds of being a male. 100% indicates a man, and 0% indicates a woman.

X = np.array(([10,65],[9,63],[70,12],[7,60],[7,63]) ,dtype=float)
Y = np.array(([1],[0],[1],[1],[0],) ,dtype=float)

#Scaling data

X = X/np.amax(X, axis=0)
Y = Y/100

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


class neuralNet(object):
    def __init__(self):
        # Define Hyperparameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3

        # Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)

    def forward(self, X):
        # Propogate inputs though network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat

    def sigmoid(self, z):
        # Apply sigmoid activation function to scalar, vector, or matrix
        return 1 / (1 + np.exp(-z))

    def sigmoidPrime(self, z):
        # Gradient of sigmoid
        return np.exp(-z) / ((1 + np.exp(-z)) ** 2)

    def costFunction(self, X, y):
        # Compute cost for given X,y, use weights already stored in class.
        self.yHat = self.forward(X)
        J = 0.5 * sum((y - self.yHat) ** 2)
        return J

    def costFunctionPrime(self, X, y):
        # Compute derivative with respect to W and W2 for a given X and y:
        self.yHat = self.forward(X)

        delta3 = np.multiply(-(y - self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)

        delta2 = np.dot(delta3, self.W2.T) * self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)

        return dJdW1, dJdW2




net = neuralNet()
prediction = net.forward(X)
cost1 = net.costFunction(X,Y)
dJdW1, dJdW2 = net.costFunctionPrime(X,Y)
print(dJdW2)


