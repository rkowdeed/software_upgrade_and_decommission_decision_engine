import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import copy
from sklearn.model_selection import train_test_split 

# Load data
data = pd.read_csv("sw_hw_asset_metric_counts.csv")
print(data.shape)
# Split up predictors and target
y = data['MEDV']
X = data.drop(columns=['MEDV'])

X_train, X_test, y_train, y_test = train_test_split(X,y , 
                                   random_state=104,  
                                   test_size=0.25,  
                                   shuffle=True) 

# Distribution of predictors and relationship with target
for col in X.columns:
    fig, ax = plt.subplots(1, 2, figsize=(6,2))
    ax[0].hist(X[col])
    ax[1].scatter(X[col], y)
    fig.suptitle(col)
    #plt.show()

def compute_cost(X, y, w, b): 
    m = X.shape[0] 
    
    f_wb = np.dot(X, w) + b
    cost = np.sum(np.power(f_wb - y, 2))
    
    total_cost = 1 / (2 * m) * cost

    return total_cost

def compute_gradient(X, y, w, b):
    m, n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.
    
    err = (np.dot(X, w) + b) - y
    dj_dw = np.dot(X.T, err)    # dimension: (n,m)*(m,1)=(n,1)
    dj_db = np.sum(err)
    
    dj_dw = dj_dw / m
    dj_db = dj_db / m
    
    return dj_db, dj_dw

def gradient_descent(X, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters):
    J_history = []
    w = copy.deepcopy(w_in)
    b = b_in
    
    for i in range(num_iters):
        dj_db, dj_dw = gradient_function(X, y, w, b)
        
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        
        cost = cost_function(X, y, w, b)
        J_history.append(cost)
        
        if i % math.ceil(num_iters/10) == 0:
            print(f"Iteration {i:4d}: Cost {J_history[-1]:8.2f}")
        
    return w, b, J_history

def plot_cost(data, cost_type):
    plt.figure(figsize=(4,2))
    plt.plot(data)
    plt.xlabel("Iteration Step")
    plt.ylabel(cost_type)
    plt.title("Cost vs. Iteration")
    plt.show()    

def predict(X, w, b):
    p = np.dot(X, w) + b
    return p

def compute_mse(y1, y2):
    return np.mean(np.power((y1 - y2),2))

iterations = 1000
alpha = 1.0e-6

w_out, b_out, J_hist = gradient_descent(X_train, y_train, 2, 2, compute_cost, compute_gradient, alpha, iterations)

y_pred = predict(X_test, w_out, b_out)

mse = compute_mse(y_test, y_pred)
print(mse)