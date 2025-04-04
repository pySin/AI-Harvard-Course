import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

model = Perceptron()
# model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=1)
# model = GaussianNB()
