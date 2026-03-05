# AI Smart Savings & Well-Being Advisor

Final project for the Building AI course

---

## Summary

The **AI Smart Savings & Well-Being Advisor** is an interactive financial planning tool built with **Python and Streamlit**. It helps users understand monthly savings, receive investment suggestions based on risk tolerance, and evaluate their financial well-being. It also includes risk simulations for assets under global conflict scenarios.  

---

## Background

Many individuals struggle to plan their finances and understand how different investment strategies affect their wealth. Common problems include:

* Not knowing how much they can save each month
* Uncertainty about investment allocations based on risk
* Lack of awareness of financial stress and well-being
* Difficulty predicting portfolio outcomes under uncertain global events  

**Motivation:** As someone interested in finance and data science, I wanted to build a tool that combines **financial calculations, risk simulations, and well-being assessment** to help users make better-informed decisions.

---

## How is it used?

1. **Input monthly income and expenses** to calculate estimated savings.  
2. **Select risk tolerance** (Low / Medium / High) to get investment allocation suggestions.  
3. **View financial well-being score** based on income and expenses.  
4. **Simulate portfolio performance** under different global conflict levels (Low, Medium, High).  
5. **Visualize results** with charts to understand potential portfolio changes.

**Users:** Individuals looking to plan their personal finances and understand the impact of investments under uncertainty.  

Example image of the dashboard (replace with your own screenshot):

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg" width="400">

---

## Data sources and AI methods

- **Data sources:** User-provided inputs (income, expenses) and simulated asset prices.  
- **AI / Methods:**  
  - Risk simulation functions for different conflict levels  
  - Financial well-being scoring  
  - Investment allocation logic based on risk tolerance  
  - Optional: future savings prediction via simple ML model  

---

## Challenges

- Does not include real market data (currently uses simulated values).  
- Simplified financial stress model; does not account for all real-life factors.  
- Ethical considerations: financial advice should not replace professional guidance.  
- Limited to a few asset types (oil, ETFs, bonds, crypto).

---

## What next?

Potential improvements to grow the project:

* Integrate real financial market data via APIs  
* Add machine learning for investment prediction  
* Improve financial well-being modeling  
* Add user account tracking and persistent data  
* Expand asset types (ETF and stock database)  

---

## Project Structure


AI_Smart_Savings_Advisor/
│
├─ app.py # Main Streamlit dashboard
├─ finance_logic.py # Savings & portfolio allocation logic
├─ wellbeing.py # Financial stress scoring model
├─ risk_simulation.py # Investment simulation under conflict scenarios
├─ ml_model.py # Future savings prediction model
├─ README.md # Project documentation
└─ venv/ # Python virtual environment (ignored)


---

## How to Run the Project

1. Clone or download the repository:

bash
git clone https://github.com/yourusername/AI_Smart_Savings_Advisor.git

Navigate to the project folder:

cd AI_Smart_Savings_Advisor

Create a virtual environment:

python -m venv venv

Activate the environment:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

Install dependencies:

pip install streamlit matplotlib

Run the application:

streamlit run app.py
Acknowledgments

Inspired by personal finance and data science projects

UI template and project guide from Reaktor Innovations & University of Helsinki

Example image: Sleeping Cat on Her Back by Umberto Salvagnin
 / CC BY 2.0

Author

Hind Rahali
Interdisciplinary Data Science and Finance Student
Interested in Data Science, Finance, and Algorithmic Investment Strategies



