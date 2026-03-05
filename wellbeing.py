# financial stress / well-being calculations
def financial_stress_score(income, expenses):

    
    if income == 0:
        return 100   # maximum stress if no income

    savings_rate = max((income - expenses) / income, 0)

    stress_score = (1 - savings_rate) * 100

    return stress_score
  
