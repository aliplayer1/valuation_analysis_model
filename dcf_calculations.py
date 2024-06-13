def calculate_dcf(financial_data, discount_rate=0.1, growth_rate=0.02, projection_years=5):
    free_cash_flows = []
    revenue = financial_data.get("revenue", 0)
    cogs = financial_data.get("cogs", 0)
    opex = financial_data.get("opex", 0)
    tax_rate = financial_data.get("tax_rate", 0) / 100
    capex = financial_data.get("capex", 0)
    depreciation = financial_data.get("depreciation", 0)
    net_income = financial_data.get("net_income", 0)
    
    initial_fcf = net_income + depreciation - capex
    free_cash_flows.append(initial_fcf)
    
    for year in range(1, projection_years + 1):
        revenue *= (1 + growth_rate)
        fcf = revenue - cogs - opex - capex + depreciation
        fcf_after_tax = fcf * (1 - tax_rate)
        free_cash_flows.append(fcf_after_tax)
    
    discounted_fcfs = [fcf / (1 + discount_rate) ** year for year, fcf in enumerate(free_cash_flows)]
    
    terminal_value = free_cash_flows[-1] * (1 + growth_rate) / (discount_rate - growth_rate)
    discounted_terminal_value = terminal_value / (1 + discount_rate) ** projection_years
    
    dcf_value = sum(discounted_fcfs) + discounted_terminal_value
    
    return dcf_value
