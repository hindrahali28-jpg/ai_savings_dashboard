# AI Smart Savings & Well-Being Advisor
import streamlit as st
import matplotlib.pyplot as plt

#     External modules 
from finance_logic import calculate_savings, investment_allocation
from wellbeing import financial_stress_score
from risk_simulation import simulate_investment
from ml_model import predict_savings_growth

#     App title 
st.title("AI Smart Savings & Well-Being Advisor")
st.write("Welcome Hind 👋")

#     User Inputs 
income = st.number_input("Monthly Income ($)", min_value=0.0)
expenses = st.number_input("Monthly Expenses ($)", min_value=0.0)
goal = st.number_input("Savings Goal ($)", min_value=0.0)
risk = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])

#     Finance Calculation 
if st.button("Calculate"):
    # Monthly savings
    savings = calculate_savings(income, expenses)
    st.write(f"Estimated monthly savings: ${savings:.2f}")
    
    # Investment allocation
    allocation = investment_allocation(risk)
    st.write("Suggested investment allocation:")
    for asset, percent in allocation.items():
        st.write(f"{asset}: {percent}%")
    
    # Financial well-being score
    if income == 0 and expenses == 0:
        st.info("Enter your income and expenses to generate your financial analysis.")
    else:
        score = financial_stress_score(income, expenses)
        st.write(f"Financial Well-Being Score: {100 - score:.1f}/100 (higher is better)")
    
    # Predicted future savings
    future_savings = predict_savings_growth(income, expenses)
    st.write(f"Predicted future savings: ${future_savings:.2f}")

#     Risk Simulation 
st.subheader("Projected Portfolio under Conflict Scenarios")

# Example asset values
portfolio_assets = {
    "Oil": 80,
    "Emerging ETF": 200,
    "Gold ETF": 190,
    "Bonds": 100,
    "Crypto": 35000
}

# Store total portfolio values for visualization
total_portfolio_values = {}

for level in ["Low", "Medium", "High"]:
    st.write(f"**{level} conflict →**")
    total_value = 0
    for asset, price in portfolio_assets.items():
        future_value = simulate_investment(price, level)
        total_value += future_value
        st.write(f"{asset}: ${future_value:.2f}")
    total_portfolio_values[level] = total_value

#      Visualization 
fig, ax = plt.subplots()
ax.bar(total_portfolio_values.keys(), total_portfolio_values.values(), color='skyblue')
ax.set_ylabel("Projected Portfolio Value ($)")
ax.set_title("Portfolio Value by Conflict Scenario")
st.pyplot(fig)
