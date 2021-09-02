import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

boston_dataset = load_boston()
boston_df = pd.DataFrame(data= boston_dataset.data , columns=boston_dataset.feature_names)
boston_df['price'] = boston_dataset.target

# X_train = np.random.uniform(1, 40, 200).reshape((-1, 1))
# X_0 = np.ones(X_train.shape[0], dtype='int8').reshape((-1, 1))
# X_all = np.append(X_0, X_train, axis=1)


class LinearRegression:
    def fit(self, X_train: np.ndarray, Y_train: np.ndarray) -> None:
        if X_train.shape[0] != Y_train.shape[0]:
            raise Exception("X , Y tafahom nadaran")
        X_0 = np.ones(X_train.shape[0], dtype='int8').reshape((-1, 1))
        X_train_temp = np.append(X_0, X_train, axis=1)
        self.W = np.matmul(np.linalg.inv(np.matmul(X_train_temp.T, X_train_temp)), np.matmul(X_train_temp.T, Y_train))
        self.coef_ = self.W[1:]
        self.intercept_ = self.W[0]

    def _predict(self, X_test: np.ndarray) -> np.ndarray:
        if X_test.shape[0] != self.coef_.shape[0]:
            raise Exception("tedad feature ha ro kamel nadadi")
        Y_predict = np.dot(X_test, self.coef_) + self.intercept_
        return Y_predict

    def predict(self, X_test):
        result = []
        for x_sample in X_test:
            result.append(self._predict(x_sample))
        return np.array(result)

    def evaluate(self, Y_test, Y_predict):
        pass

X = boston_df.iloc[:, :-1].values
y = boston_df.iloc[:,-1].values
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.4 , random_state=85)

lr = LinearRegression()
lr.fit(X_train, y_train)
prediction = lr.predict(X_test)
print(lr.coef_)
print(lr.intercept_)

plt.hist(y_test-prediction)
plt.show()