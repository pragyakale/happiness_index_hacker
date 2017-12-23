# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as smf
from sklearn import linear_model
from scipy.optimize import minimize
import matplotlib.pyplot as plt; plt.rcdefaults()

# this allows plots to appear directly in the notebook
%matplotlib inline

data=pd.read_csv('hp.csv',index_col=0)
#Linear Regression
results = smf.ols(formula='happiness ~ sleep + work + learn + socialise', data=data).fit()

#finding a maxima

#defining the function
def fun(v):
    a,b,c,d=v
    return -1*(a*results.params["sleep"]+b*results.params["work"]+c*results.params["learn"]+d*results.params["socialise"]+results.params["Intercept"])

bounds = [(10, 11), (0, 100), (10, 100),(10,100)]
def cons1(x):
    return -x[0]-x[1]-x[2]-x[3]+100
con = {'type': 'ineq', 'fun': cons1}
initial_guess = [6, 1, 1, 1]
result = minimize(fun, initial_guess,bounds=bounds,constraints=con)
if result.success:
    fitted_params = result.x
    print(fitted_params)
    objects = ('Sleep', 'Work', 'Learn', 'Socialise')
    y_pos = np.arange(len(objects))
    performance=fitted_params
    plt.bar(y_pos, performance, align='center', alpha=1)
    plt.xticks(y_pos, objects)
    
else:
    raise ValueError(result.message)

