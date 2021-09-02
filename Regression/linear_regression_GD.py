import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salary_df_old = pd.read_csv("./data/Salary_Data.csv")
sample_size = salary_df_old.shape[0]

from sklearn import preprocessing

x = salary_df_old.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
salary_df = pd.DataFrame(x_scaled, columns=["YearsExperience", "Salary"])


class LR_GD_Salary:

    def compute_cost_function(self, w_0, w_1):
        w_1_x = np.dot(w_1, salary_df["YearsExperience"])
        hypothesis_function = w_0 + w_1_x
        loss_particle = np.subtract(hypothesis_function, salary_df["Salary"])
        loss = np.dot(loss_particle, loss_particle)
        cost_function = np.sum(loss) * 1 / (2 * sample_size)
        return cost_function

    def gradient_descent(self, w_0, w_1, intercept=True):
        w_1_x = np.dot(w_1, salary_df["YearsExperience"])
        hypothesis_function = w_0 + w_1_x
        loss_particle = np.subtract(hypothesis_function, salary_df["Salary"])
        if not intercept:
            loss_particle = np.dot(loss_particle, salary_df["YearsExperience"])
        return np.sum(loss_particle) * 1 / (sample_size)

    def compute_cost_over_iterarion(self, linear_rate, iterarion):
        cost = []
        w_0 = 0
        w_1 = 0

        for index in range(iterarion):
            temp_0 = w_0 - linear_rate * self.gradient_descent(w_0, w_1)
            temp_1 = w_1 - linear_rate * self.gradient_descent(w_0, w_1, False)

            w_0 = temp_0
            w_1 = temp_1

            cost.append(self.compute_cost_function(w_0, w_1))
        return cost


lr_GD = LR_GD_Salary()
plt.plot(lr_GD.compute_cost_over_iterarion(0.5, 2000))
plt.show()
