import re

def parse_financial_data(text):
    financial_data = {}
    patterns = {
        "revenue": r"Revenue[:\s]+(\d+\.?\d*)",
        "cogs": r"Cost of Goods Sold[:\s]+(\d+\.?\d*)",
        "opex": r"Operating Expenses[:\s]+(\d+\.?\d*)",
        "tax_rate": r"Tax Rate[:\s]+(\d+\.?\d*)%",
        "capex": r"Capital Expenditures[:\s]+(\d+\.?\d*)",
        "depreciation": r"Depreciation[:\s]+(\d+\.?\d*)",
        "net_income": r"Net Income[:\s]+(\d+\.?\d*)",
        "ebitda": r"EBITDA[:\s]+(\d+\.?\d*)"
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            financial_data[key] = float(match.group(1))
    
    return financial_data

def calculate_financial_metrics(financial_data):
    metrics = {}
    metrics["Gross Profit"] = financial_data.get("revenue", 0) - financial_data.get("cogs", 0)
    metrics["Operating Income"] = metrics["Gross Profit"] - financial_data.get("opex", 0)
    metrics["EBITDA"] = financial_data.get("ebitda", 0)
    metrics["Net Income"] = financial_data.get("net_income", 0)
    return metrics
