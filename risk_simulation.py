# regional conflict impact logic
conflict_impact = {
    "Low": 1.01,    # +1% change
    "Medium": 1.05, # +5% change
    "High": 1.1     # +10% change
}

def simulate_investment(asset_price, conflict_level):
    return asset_price * conflict_impact[conflict_level]