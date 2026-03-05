def calculate_savings(income, expenses):
    return income - expenses


def investment_allocation(risk):

    if risk == "Low":
        allocation = {"Bonds": 70, "Stocks": 20, "Cash": 10}

    elif risk == "Medium":
        allocation = {"Bonds": 40, "Stocks": 50, "Cash": 10}

    elif risk == "High":
        allocation = {"Bonds": 10, "Stocks": 80, "Cash": 10}

    return allocation
