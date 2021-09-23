# classifier that detect iris-Virginica type base only in petal width

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# iris = datasets.load_iris()
# X = iris["data"][:, 3:]
# y = (iris["target"] == 2).astype('int')

# lr = LogisticRegression(C=10)
# lr.fit(X, y)

# X_test = np.linspace(1, 3, 500).reshape(-1, 1)
# y_predict = lr.predict_proba(X_test)
# print(y_predict)
# plt.plot(X_test, y_predict[:, 1], "g-", label="Virginica")
# plt.plot(X_test, y_predict[:, 0], "r:", label="Not Virginica")

# plt.show()


# classifier that detect iris-Virginica type base only in petal width
iris = datasets.load_iris()
X = iris["data"][:, 2:]
y = iris["target"]


lr_softmax = LogisticRegression(
    multi_class="multinomial", solver="lbfgs", C=15)
lr_softmax.fit(X, y)

X_test = np.linspace(1, 5, 500).reshape(-1, 2)
np.random.shuffle(X_test)
y_predict_prob = lr_softmax.predict_proba(X_test)
y_predict = lr_softmax.predict(X_test)
print(X_test[y_predict == 0])
print(y_predict == 1)
print(y_predict == 2)
plt.scatter(X_test[y_predict == 0][:, 0],
            X_test[y_predict == 0][:, 1], c="red", label="versicolor")
plt.scatter(X_test[y_predict == 1][:, 0],
            X_test[y_predict == 1][:, 1], c="green", label="setosa")
plt.scatter(X_test[y_predict == 2][:, 0],
            X_test[y_predict == 2][:, 1], c="blue", label="viginica")


plt.show()
