# import sys
# import subprocess
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sklearn'])
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
df_x = pd.DataFrame(housing.data, columns = housing.feature_names)
df_y = pd.DataFrame(housing.target)
print('\ndescribe = \n')
df_x.describe()
reg = linear_model.LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.33, random_state=42)
reg.fit(x_train, y_train)
print(f"\nreg_coef =\n {reg.coef_}")
y_pred = reg.predict(x_test)
print(f"\ny_pred = {y_pred}")
# y_pred[2]
# y_test[0]
npmean = np.mean((y_pred-y_test)**2)
print(f"\nnpmean = {npmean}")
mse = mean_squared_error(y_test, y_pred)
print(f"\nmse = {mse}")





