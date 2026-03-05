from sklearn.linear_model import LinearRegression
import numpy as np

def predict_savings_growth(income, expenses):

    # Example historical data
    X = np.array([[2000],[3000],[4000],[5000]])
    y = np.array([200, 400, 700, 1200])

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[income]])

    return prediction[0]
