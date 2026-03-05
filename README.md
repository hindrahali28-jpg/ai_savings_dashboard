# Project description

# AI Smart Savings & Well-Being Advisor

## Project Overview

The **AI Smart Savings & Well-Being Advisor** is an interactive financial planning tool built with **Python and Streamlit**.
It helps users understand their monthly savings, receive investment suggestions based on risk tolerance, and evaluate their financial well-being.

The project also includes **risk simulation models** that estimate how global conflict scenarios could impact assets such as oil prices and emerging market ETFs.

This project combines **finance, data science, and behavioral well-being** to help individuals make better financial decisions.


## Summary 
### Features:

### 1. Savings Calculator

Users input:

* Monthly income
* Monthly expenses

The app calculates estimated monthly savings.

### 2. Investment Allocation

Based on risk tolerance (Low / Medium / High), the app suggests an investment portfolio allocation.

Example:

Low Risk:

* Bonds
* Stocks
* Cash

Medium Risk:

* Balanced portfolio

High Risk:

* Higher stock exposure.

### 3. Financial Well-Being Score

A simple financial stress model estimates financial well-being based on the relationship between income and expenses.

Higher scores indicate stronger financial stability.

### 4. Global Conflict Risk Simulation

The project simulates how assets might behave under different geopolitical conflict levels:

* Low conflict
* Medium conflict
* High conflict

Assets simulated:

* Oil prices
* Emerging market ETFs

### 5. Data Visualization

The app generates visual charts to help users understand projected portfolio changes under different risk scenarios.

---

## Technologies Used

* Python
* Streamlit
* Matplotlib
* Financial modeling logic
* Risk simulation

---

## Project Structure

AI_Smart_Savings_Advisor/

app.py → Main Streamlit dashboard
finance_logic.py → Savings + portfolio allocation logic
wellbeing.py → Financial stress scoring model
risk_simulation.py → Investment simulation under conflict scenarios
README.md → Project documentation
venv/ → Python virtual environment

---

## How to Run the Project

### 1. Clone or download the repository

### 2. Navigate to the project folder

```
cd AI_Smart_Savings_Advisor
```

### 3. Create a virtual environment

```
python -m venv venv
```

### 4. Activate the environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 5. Install dependencies

```
pip install streamlit matplotlib
```

### 6. Run the application

```
streamlit run app.py
```

The dashboard will open in your browser.

---

## Future Improvements

* Add real financial market data (API integration)
* Add machine learning for investment prediction
* Improve financial well-being modeling
* Add user account tracking
* Add ETF and stock database

---

## Author

Hind Rahali
Interdisciplinary Data Science and Finance Student
Interested in **Data Science, Finance, and Algorithmic Investment Strategies**


