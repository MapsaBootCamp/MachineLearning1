import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

x = 3 - 4 * np.random.normal(0, 1, 20)
y = x - 2 * (x ** 2) + 2 * (x ** 3) + np.random.normal(-3, 3, 20)

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

polynomial_features = PolynomialFeatures(degree=3)
x_polynomial = polynomial_features.fit_transform(x)

model = LinearRegression()
model.fit(x_polynomial, y)
# y_linear = model.predict(x)
y_polynomial_pred = model.predict(x_polynomial)

rmse = np.sqrt(mean_squared_error(y, y_polynomial_pred))
r2 = r2_score(y, y_polynomial_pred)
print("root mean squared error: ", rmse)
print("coefficient of determination: ", r2)

plt.scatter(x, y)
sorted_zip = sorted(zip(x, y_polynomial_pred), key=lambda x: x[0])
x, y_polynomial_pred = zip(*sorted_zip)
plt.plot(x, y_polynomial_pred, color='g')
plt.show()
